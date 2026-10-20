import streamlit as st
import streamlit.components.v1 as components

# Sayfa Yapılandırması
st.set_page_config(
    page_title="LOCUS - Dijital Ajanda",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML Kodunu oku ve ekrana yansıt
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Tam ekran HTML Bileşeni
components.html(html_code, height=900, scrolling=True)
