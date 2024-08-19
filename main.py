import streamlit as st

st.set_page_config(
    page_title="Análisis de Sentimientos",
    page_icon=":speech_ballon:"
)

home_page = st.Page("home.py", title="Home", icon=":material/home:")
analisis_page = st.Page("analisis.py", title="Análisis de Sentimientos", icon=":material/area_chart:")

pg = st.navigation([home_page, analisis_page])
pg.run()