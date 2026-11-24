"""Portfolio de Zineb Ennakhla, servi avec Streamlit.

Le site lui-même est dans site/index.html (HTML/CSS/JS).
Ce fichier l'affiche en plein écran dans Streamlit.
"""
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

SITE = Path(__file__).parent / "site"

st.set_page_config(
    page_title="Zineb Ennakhla | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Cacher l'interface Streamlit et afficher le site en plein écran
st.markdown(
    """
    <style>
      header, footer, #MainMenu, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }
      .stApp, [data-testid="stAppViewContainer"] { background: #0e1b20; }
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important; max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { display: block; width: 100vw !important; height: 100vh !important; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


def data_uri(path: Path, mime: str) -> str:
    """Transforme un fichier en lien 'data:' pour l'intégrer directement dans la page."""
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


@st.cache_data
def build_page(version: float) -> str:
    # "version" = date de modification des fichiers : quand index.html change,
    # le cache est ignoré et la nouvelle version s'affiche.
    html = (SITE / "index.html").read_text(encoding="utf-8")
    # Dans Streamlit, la page ne peut pas charger les fichiers voisins :
    # on intègre donc la photo et le CV directement dans le HTML.
    html = html.replace('src="avatar.jpg"', f'src="{data_uri(SITE / "avatar.jpg", "image/jpeg")}"')
    html = html.replace(
        'href="CV_Zineb_Ennakhla.pdf"',
        f'href="{data_uri(SITE / "CV_Zineb_Ennakhla.pdf", "application/pdf")}"',
    )
    # Images des projets (dossier site/projects)
    for img in sorted((SITE / "projects").glob("*.jpg")):
        html = html.replace(f'src="projects/{img.name}"', f'src="{data_uri(img, "image/jpeg")}"')
    return html


version = max(f.stat().st_mtime for f in SITE.rglob("*") if f.is_file())
components.html(build_page(version), height=900, scrolling=True)
