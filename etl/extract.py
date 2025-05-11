import pandas as pd
import os

#Fonction pour importé le fichier csv et le traités
def extract_data(filepath):
    #Variable dataframe pour lire le csv
    df = pd.read_csv(filepath)
    #Lecture des 5 premiers résultats
    print("print des 5 premiere valeur", df[:5])
    print("Fais la meme choses que df[:5]", df.head())

    #Lecture du tableau
    print("Forme du tableau", df.shape)

    return df

extract_data("data/simulated/sensor_data.csv")
