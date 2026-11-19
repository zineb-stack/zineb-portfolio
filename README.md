# Portfolio – Zineb Ennakhla

Data Analyst · Data Scientist · Développeuse IA — Tanger, Maroc

Site portfolio bilingue (FR/EN) avec mode clair et sombre, publié avec Streamlit.

## Structure
```
zineb-portfolio/
├── app.py               # affiche le site dans Streamlit
├── requirements.txt     # dépendances (streamlit)
├── .streamlit/config.toml
└── site/
    ├── index.html       # le site (HTML, CSS, JS)
    ├── avatar.jpg
    └── CV_Zineb_Ennakhla.pdf
```

## Branches
- **main** : la version MVP, stable, publiée en ligne
- **dev** : les modifications en cours ; fusionnées dans main quand elles sont prêtes

## Lancer en local
```bash
pip install -r requirements.txt
streamlit run app.py
```
