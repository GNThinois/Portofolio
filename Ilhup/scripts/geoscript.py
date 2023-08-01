from ratelimiter import RateLimiter
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
from tqdm import tqdm
from time import sleep

import pandas as pd
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'logins')))
import logins

api_key = logins.openrouteservice_api_key

# Créer un rate limiter pour les requêtes à Nominatim
geocode_limiter = RateLimiter(max_calls=1, period=1)  # 1 requête par seconde
# Créer un rate limiter pour les requêtes à openrouteservice
route_limiter = RateLimiter(max_calls=2, period=1)  # 2 requêtes par seconde

def calculate_distance(address1, address2, pbar, max_retries=3):
    geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)

    try:
        location1 = geolocator.geocode(address1)
    except GeocoderTimedOut:
        for i in range(max_retries):
            try:
                sleep(2 ** i)  # Exponential back-off
                location1 = geolocator.geocode(address1)
            except GeocoderTimedOut:
                continue
            break  # If successful, break out of retry loop

    try:
        location2 = geolocator.geocode(address2)
    except GeocoderTimedOut:
        for i in range(max_retries):
            try:
                sleep(2 ** i)  # Exponential back-off
                location2 = geolocator.geocode(address2)
            except GeocoderTimedOut:
                continue
            break  # If successful, break out of retry loop

    if location1 is not None and location2 is not None:
        p1 = (location1.latitude, location1.longitude)
        p2 = (location2.latitude, location2.longitude)
        distance = geodesic(p1, p2).km
        pbar.update()
        return distance
    else:
        return None


def get_postal_code(city_name):
    response = requests.get(f"https://api-adresse.data.gouv.fr/search/?q={city_name}&limit=1")
    data = response.json()
    return data['features'][0]['properties']['postcode']

def calculate_driving_distance(address1, address2, pbar=None):
    """
    This function calculates and returns the driving distance (in kilometers) between two addresses.

    Parameters:
    address1 (str): The first address as a string. It should include street name, city, and country.
    address2 (str): The second address as a string. It should include street name, city, and country.

    Returns:
    float: The driving distance between address1 and address2 in kilometers.
    If one or both the addresses cannot be geocoded, or if the routing API request fails,
    it returns a string with an error message.
    """

    geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)

    with geocode_limiter:
        location1 = geolocator.geocode(address1)
    with geocode_limiter:
        location2 = geolocator.geocode(address2)

    if not location1 or not location2:
        # return a large number so that this row is not selected by nsmallest
        if pbar is not None:
            pbar.update()
        return 1e6

    coord1 = (location1.latitude, location1.longitude)
    coord2 = (location2.latitude, location2.longitude)

    # Utiliser le rate limiter lors de l'appel à l'API openrouteservice
    with route_limiter:
        response = requests.get(f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={coord1[1]},{coord1[0]}&end={coord2[1]},{coord2[0]}")
    if response.status_code != 200:
        # return a large number so that this row is not selected by nsmallest
        if pbar is not None:
            pbar.update()
        return 1e6

    data = response.json()

    # The distance is returned in meters, so we convert it to kilometers
    distance = data['features'][0]['properties']['summary']['distance'] / 1000
    if pbar is not None:
        pbar.update()

    return round(distance, 1)


def closest_ide(address, df, num_closest):
    """
    Calculate the distance from the given address to all IDE in the dataframe,
    and return the num_closest IDEs.

    Parameters:
    address (str): The given address as a string.
    df (pd.DataFrame): The dataframe with IDE data.
    num_closest (int): The number of closest IDEs to return.

    Returns:
    pd.DataFrame: The num_closest closest IDEs to the given address.
    """

    # Create a new column 'full_address' in the dataframe
    df['full_address'] = df['Rue'] + ', ' + df['CP'].astype(str) + ', ' + df['Ville'] + ', France'

    # Create a 'full_name' column
    df['full_name'] = df['Prénom'] + ' ' + df['Nom']

    # Create a progress bar
    pbar = tqdm(total=len(df)*2, desc="Calculating distances", ncols=100)

    # Calculate the geodesic distance from the given address to each IDE
    df['distance_geodesic'] = df['full_address'].apply(lambda x: calculate_distance(address, x, pbar))

    # Calculate the driving distance from the given address to each IDE
    df['distance_driving'] = df['full_address'].apply(lambda x: calculate_driving_distance(address, x, pbar))

    # Update the progress bar
    pbar.update()

    # Close the progress bar
    pbar.close()

    # Sort the dataframe by distance and select the num_closest IDEs
    closest_ides_geodesic = df.nsmallest(num_closest, 'distance_geodesic')
    closest_ides_driving = df.nsmallest(num_closest, 'distance_driving')

    # Return only the columns you're interested in
    return closest_ides_geodesic[['full_name', 'full_address', 'distance_geodesic']], closest_ides_driving[['full_name', 'full_address', 'distance_driving']]


def verify_data(df):
    # Verify the 'Prénom' and 'Nom' columns.
    # Here we just check if they are of type string, but you might want to do a more complex check.
    for index, value in df[['Prénom', 'Nom']].stack().items():
        if not isinstance(value, str):
            print(f"Error at index {index}: {value} is not a string.")

    # Verify the 'Rue' column. Here we just check if it's a string.
    for index, value in df['Rue'].items():
        if not isinstance(value, str):
            print(f"Error at index {index}: {value} is not a string.")

    # Verify the 'CP' column. Here we just check if it's an integer.
    for index, value in df['CP'].items():
        if not isinstance(value, (int, str)):
            print(f"Error at index {index}: {value} is not an integer or a string.")

    # Verify the 'Ville' column. Here we just check if it's a string.
    for index, value in df['Ville'].items():
        if not isinstance(value, str):
            print(f"Error at index {index}: {value} is not a string.")

if __name__ == '__main__':
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(os.path.join(os.path.dirname(__file__), '..', 'assets', 'data', 'IDE.xlsx'))

    # Verify the data
    verify_data(df)
    print("Data verified")

    address = "Saint-Astier, 24110, France"
    num_closest = 5  # The number of closest IDEs to return

    closest_ides = closest_ide(address, df, num_closest)
    print(closest_ides)
