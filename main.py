import streamlit as st
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from transformers import pipeline
from pysentimiento import create_analyzer

# Configuración de la aplicación
st.title("Análisis de Sentimientos en Comentarios de Redes Sociales")
st.write("Ingrese un comentario para analizar su sentimiento. ")

# Cargue del modelo de análisis de sentimientos
analyzer = create_analyzer(task="sentiment", lang="es")

# Formulario para ingresar comentarios
comment = st.text_area("Comentario")

if st.button("Analizar sentimiento"):
    if comment:
        result = analyzer.predict(comment)
        st.write(f'Sentimiento: {result.output}')
        st.write(f'Scores: {result.probas}')
    else:
        st.write("Por favor, ingrese un comentario para analizar.")