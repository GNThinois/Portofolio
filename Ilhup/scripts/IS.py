import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def rename_columns(df):
    df.columns = ["Contact : Numéro de campagne", "Contact : Matricule", "Contact : Date de naissance", "Contact : Code sexe ",
                  "Contact : age", "Contact : Nom", "Contact : Prénom", "Contact : Nom jeune fille", "Contact : Adresse",
                  "Contact : Complément d'adresse", "Contact : Code postal adhérent", "Contact : Ville adhérent", "Contact : Localité",
                  "Contact : Code commune", "Contact : Libellé commune", "Contact : Code canton 2014", "Contact : Libellé canton 2014",
                  "Contact : Département lien unique", "Contact : NIL", "Contact : Adresse e-mail", "Contact : Téléphone (domicile)",
                  "Contact : Téléphone mobile principal", "Contact : Code statut", "Contact : Statut", "Contact : Numéro ADELI MT",
                  "Contact : Nom MT", "Contact : Prénom MT", "Contact : Adresse MT", "Contact : Cplt d'adresse MT", "Contact : Code postal MT",
                  "Contact : Ville MT"]

    return df

def change_columns_format(df):

    return df
def add_columns(df):
    tmp = "Contact : Type d'enregistrement du contact"
    return df



def run(df):
    df = rename_columns(df)
    df = change_columns_format(df)
    df = add_columns(df)
    return df
