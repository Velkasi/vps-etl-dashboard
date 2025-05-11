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

    #df_valid = dataframe[(dataframe ["temperature"] supérieure ou égale a 30 et (dataframe["temperature"] inferieure ou égale a 100)
    df_valid = df[(df["temperature"] >= 30) & (df["temperature"] <= 100 )]
    #print("df_valide", df_valid)

    #temperature de rejet = (dataframe["temperature"] inférieur a 30) ou (df["temperature"] superieur a 100)
    temp_rejets = (df["temperature"] < 30) | (df["temperature"] > 100)
    #print("temp_rejets", temp_rejets)

    #df_rejets = dataframe[temp_rejets] On extrait les lignes rejetées de df en appliquant le masque temp_rejets
    df_rejets = df[temp_rejets]
    #print("df_rejets", df_rejets)

    nb_lignes_rejetées = df_rejets.shape[0]

    print(f"Sauvegarde des temperature anormale en cour...: {nb_lignes_rejetées} lignes")

    #On envoie les lignes df_rejets vers un csv
    df_rejets.to_csv("data/intermediate/dropped_temperature.csv", index=False)

    print(f"Sauvegarde terminée: {nb_lignes_rejetées} lignes")

    nb_rejetees = df.shape[0] - df_valid.shape[0]

    print(f"Lignes supprimées (température hors normes) : {nb_rejetees}")

    print(f"Lignes supprimées (valeurs manquantes) : {initial_shape[0] - final_shape[0]}")

#dataframe_raw = le chemin du csv
df_raw = extract_data("data/simulated/sensor_data.csv")

#dataframe_clean = la fonction qui netoie la donnée de df_raw
df_clean = transform_data(df_raw)