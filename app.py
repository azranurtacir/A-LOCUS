{\rtf1\ansi\ansicpg1254\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import streamlit.components.v1 as components\
\
# Sayfa Yap\uc0\u305 land\u305 rmas\u305 \
st.set_page_config(\
    page_title="LOCUS - Dijital Ajanda",\
    page_icon="\uc0\u55357 \u56534 ",\
    layout="wide",\
    initial_sidebar_state="collapsed"\
)\
\
# HTML Kodunu oku ve ekrana yans\uc0\u305 t\
with open("index.html", "r", encoding="utf-8") as f:\
    html_code = f.read()\
\
# Tam ekran HTML Bile\uc0\u351 eni\
components.html(html_code, height=900, scrolling=True)}