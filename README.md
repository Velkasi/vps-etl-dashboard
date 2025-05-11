# vps-etl-dashboard

Visualisation du Projet 

vps-etl-dashboard/
│
├── data/                      # Dossiers pour les fichiers de données
│   ├── raw/                  # Fichiers bruts (capteurs)
│   └── processed/            # Fichiers transformés
│
├── etl/                      # Code pour extract / transform / load
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── dashboard/                # Ton dashboard Streamlit (ou autre)
│   └── app.py
│
├── scripts/                  # Scripts ponctuels (ex: génération)
│   └── generate_data.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── run_etl.py                # Orchestrateur ETL