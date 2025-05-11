# vps-etl-dashboard

# Projet ETL Capteurs Industriels

Ce projet simule, traite et visualise des données de capteurs industriels (température) sur 30 jours.

## Installation
pip install -r requirements.txt

## CSV de simultation pour ETL
data/simulated/sensor_data.csv
Ce fichier CSV est versionné uniquement à des fins de démonstration. Dans un vrai projet, il serait stocké ailleurs (S3, BDD, etc.).


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