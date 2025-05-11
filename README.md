# vps-etl-dashboard

# Projet ETL Capteurs Industriels

Ce projet simule, traite et visualise des données de capteurs industriels (température) sur 30 jours.

## Installation
pip install -r requirements.txt

-------------------------------------------

**Combien de mesures aura un seul capteur sur 30 jours à raison d’une toutes les 10 minutes ?**

6 (mesure) * 24 (h/jour) * 30 (jours) = 4320 mesures par capteur

**Combien de lignes aura ton fichier si tu as 100 capteurs ?**

100 (capteur) * 4320 (lignes) = 432 000 lignes

**Quelles seront les colonnes de ton tableau (DataFrame) ?**

nom de colonne + valeur et type : sensor_id(str) "sensor_001" / timestamp(datetime) 2025-08-12 14:30:00 / températures (float) 50.4

--------------------------------------------

**Brouillon de code a l'écris (no code)**

En premier lieu, je génère les sensor_id (donc 100), ensuite je génére un timestamp aléatoire comprise entre 2 date et je termine pas générés une temperature aleatoire pour chaque sensor_id.

**CORRECTION**

1. Créer une liste de 100 capteurs

Format : sensor_001, sensor_002, ..., sensor_100


2. Créer une série de timestamps

Espacés toutes les 10 minutes

Entre start_date = aujourd’hui - 30 jours et end_date = aujourd’hui

Tu obtiendras 4320 timestamps


3. Associer chaque capteur à tous les timestamps

Tu auras donc 100 × 4320 = 432,000 lignes

Chaque capteur a exactement la même série de temps


4. Générer une température aléatoire pour chaque ligne

Par exemple : entre 45°C et 55°C (ou autour d’une moyenne, ex : 50 ± 5)


5. Construire un DataFrame avec les colonnes :

timestamp, sensor_id, temperature


6. Sauvegarder ce DataFrame au format CSV dans data/raw/sensor_data.csv

-----------------------------------------

vps-etl-dashboard/
│
├── data/                      # Dossiers de données (ignorés par Git)
│   ├── raw/                  # Données brutes simulées
│   └── processed/            # Données transformées (par l'ETL)
│
├── etl/                      # Composants du pipeline ETL
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── dashboard/                # Ton app Streamlit ou autre
│   └── app.py
│
├── scripts/                  # Scripts ponctuels (simulateur, helpers)
│   └── generate_data.py
│
├── tests/                    # Tests unitaires (plus tard)
│   └── test_etl.py
│
├── .gitignore
├── requirements.txt          # Dépendances Python
├── run_etl.py                # Point d’entrée du pipeline ETL
├── README.md                 # Présentation du projet
└── LICENSE                   # (optionnel) Licence de ton code