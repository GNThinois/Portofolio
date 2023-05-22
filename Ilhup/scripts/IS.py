import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def rename_columns(df):
    # Replace special characters
    df = df.replace(to_replace=['^"','"$','";"',';"'], value=['','',';',';'], regex=True)
    df = df[df.columns[0]].str.split(';', expand=True)
    df.columns = [
        "Contact : Numéro de campagne", "Contact : Matricule", "Contact : Date de naissance", "Contact : Code sexe",
        "Contact : age", "Contact : Nom", "Contact : Prénom", "Contact : Nom jeune fille", "Contact : Adresse",
        "Contact : Complément d'adresse", "Contact : Code postal adhérent", "Contact : Ville adhérent", "Contact : Localité",
        "Contact : Code commune", "Contact : Libellé commune", "Contact : Code canton 2014", "Contact : Libellé canton 2014",
        "Contact : Département lien unique", "Contact : NIL", "Contact : Adresse e-mail", "Contact : Téléphone (domicile)",
        "Contact : Téléphone mobile principal", "Contact : Code statut", "Contact : Statut", "Contact : Numéro ADELI MT",
        "Contact : Nom MT", "Contact : Prénom MT", "Contact : Adresse MT", "Contact : Cplt d'adresse MT", "Contact : Code postal MT",
        "Contact : Ville MT"
    ]
    return df

def change_columns_format(df):
    phone_numbers = []
    postal_codes = []
    dates = []
    various_number = []

    print(phone_numbers)
    for col in phone_numbers:
        df[col] = df[col].str.replace('\D', '', regex=True)  # Remove non-numeric characters
        df[col] = df[col].str.zfill(10)  # Pad with zeros to ensure 10 digits

    for col in postal_codes:
        df[col] = df[col].astype(str).str.zfill(5)  # Ensure 5 digits

    for col in dates:
        df[col] = pd.to_datetime(df[col], errors='coerce')  # Convert to date format

    for col in various_number:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric format

    return df



def add_columns(df):
    tmp = "Contact : Type d'enregistrement du contact"
    val = "01209000000ZwXHAA0"

    # Drop rows where all columns are NaN
    df = df.dropna(how='all')

    # Add the new column
    df[tmp] = val

    return df




def run(df):
    df = rename_columns(df)
    print("ok column names")
    df = change_columns_format(df)
    print("ok format")
    df = add_columns(df)
    print("ok added column")

    return df

if __name__ == "__main__":
    input_file_path = r'C:\Users\Thinois\Desktop\MSA\1.csv'
    output_folder_path = r'C:\Users\Thinois\Desktop\MSA\FichiersOK'

    df = pd.read_csv(input_file_path)
    df = run(df)

    output_file_path = output_folder_path + r'\output.csv'
    df.to_csv(output_file_path, index=False)
    print(f"Saved output to: {output_file_path}")