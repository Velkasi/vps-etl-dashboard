import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from etl.extract import extract_data

#Fonction transform_data pour nettoyer la donnée
def transform_data(df):

    #df.shape te donne (lignes, colonnes)
    initial_shape = df.shape

    #Identifier les lignes à supprimer (Pas compris)
    rows_with_na = df[df.isna().any(axis=1)]

    #Supprime les NaN
    df = df.dropna()

    # Sauvegarder ces lignes
    os.makedirs("data/intermediate", exist_ok=True)

    #Les lignes supprimés to csv vers le chemin données
    rows_with_na.to_csv("data/intermediate/dropped_na_rows.csv", index=False)

    #Permet de faire la comparaison avec le initial_shape
    final_shape = df.shape

    print(f"Lignes supprimées (valeurs manquantes) : {initial_shape[0] - final_shape[0]}")

#dataframe_raw = le chemin du csv
df_raw = extract_data("data/simulated/sensor_data.csv")

#dataframe_clean = la fonction qui netoie la donnée de df_raw
df_clean = transform_data(df_raw)