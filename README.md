ATS/
│
├── backend/                    # Dossier pour l'application Flask
│   ├── app.py                  # Point d'entrée principal pour démarrer le serveur Flask
│   ├── models.py               # Définitions des modèles SQLAlchemy
│   ├── routes.py               # Routes et endpoints API Flask
│   ├── config.py               # Configuration de l'application Flask
│   └── __init__.py             # Initialisation du module Flask
│
├── frontend/                   # Dossier pour l'application Streamlit
│   ├── app.py                  # Point d'entrée principal pour démarrer Streamlit
│   ├── pages/                  # Dossier pour les différentes pages Streamlit
│   │   ├── add_candidate.py    # Page pour ajouter des candidats
│   │   ├── update_candidate.py # Page pour mettre à jour des candidats
│   │   └── view_candidates.py  # Page pour afficher les candidats
│   ├── utils.py                # Fonctions utilitaires pour Streamlit
│   └── config.py               # Configuration de Streamlit (optionnelle)
│
├── data/                       # Dossier pour les fichiers de base de données ou autres données persistantes
│   └── ats.db                  # Fichier de base de données SQLite
│
├── requirements.txt            # Fichier des dépendances Python
└── README.md                   # Documentation du projet
