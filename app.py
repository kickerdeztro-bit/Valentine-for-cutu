import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Valentine Surprise 💖", layout="wide")

html = Path("valentine.html").read_text(encoding="utf-8")

st.components.v1.html(html, height=900, scrolling=True)