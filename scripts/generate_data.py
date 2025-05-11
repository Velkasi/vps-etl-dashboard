import pandas as pd
import numpy as np
import sqlalchemy
import datetime
import os

#Test si le dossier data/simulated exist
os.makedirs("data/simulated", exist_ok=True)

#Création d'une liste sensors
sensors = []
print("Liste vide",sensors)

#Pour i dans la porté de (1 a 101)
for i in range(1,101):
    #le nom de sensor = f-string "sensor_" et on met l'index voulu, ici i:03
    sensor_name = f"sensor_{i:03}"
    #Stock les noms dans la liste sensors
    sensors.append(sensor_name)
    print(sensor_name)

print("Liste remplis", sensors)

#Definir la date de début et de fin
end_date = datetime.datetime.now() 
start_date = end_date - datetime.timedelta(days=30)

#Generation d'une serie de timestamp pour les capteurs avec panda
timestamp = pd.date_range(start=start_date, periods=4320, freq='10min')
print("timestamp",timestamp[:5])
print(len(timestamp))

#Répétition avec Numpy.repeat
sensor_ids = np.repeat(sensors, 4320)
print(len(sensor_ids))

#Copie la liste entierement avec Numpy.tile(timestamps, nombre_de_fois)
timestamps_repeated = np.tile(timestamp, 100)
print(len(timestamps_repeated))

#Generation d'une temperature (courbe en cloche) loc = moyenne, scale = ecart type, size = valeur par ligne
temperature = np.random.normal(loc=70, scale=5, size=432000)
print(temperature[:5], min(temperature), max(temperature))

dataframe = pd.DataFrame({
    'timestamp' : timestamps_repeated,
    'sensor_id' : sensor_ids,
    'temperature' : temperature
})

print(dataframe.head())
print(dataframe.shape)

print("Enregistrement du fichier...")

#Création du csv a partir du dataframe en enlevant l'index
dataframe.to_csv("data/simulated/sensor_data.csv", index=False)

print("Fichier enregistré avec succès.")
