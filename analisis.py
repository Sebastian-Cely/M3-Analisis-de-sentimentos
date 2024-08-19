import streamlit as st
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" # Necesario para evitar incompatiblidades 
from transformers import pipeline
from pysentimiento import create_analyzer


# Configuración de la página
st.title("Análisis de Sentimientos")
st.write("Ingrese un comentario para analizar su sentimiento. ")

# Cargue del modelo de análisis de sentimientos
analyzer = create_analyzer(task="sentiment", lang="es")

# Formulario para ingresar comentarios
comment = st.text_area("Comentario")

if st.button("Analizar sentimiento"):
    if comment:
        result = analyzer.predict(comment)
        st.header("Resultados", divider=True)
        
        if result.output == "NEG":
            st.markdown(f"#### Sentimiento identificado: 🔴 Comentario Negativo")
        elif result.output == "NEU":
            st.markdown(f"#### Sentimiento identificado: 🟡 Comentario Neutral")
        elif result.output == "POS":
            st.markdown(f"#### Sentimiento identificado: 🟢 Comentario Positivo")
        
        st.markdown("#### Puntajes:")
        st.write(f"🔴 Negativo: {round(result.probas['NEG'] * 100, 1)} %")
        st.write(f"🟡 Neutral: {round(result.probas['NEU'] * 100, 1)} %")
        st.write(f"🟢 Positivo: {round(result.probas['POS'] * 100, 1)} %")
        
    else:
        st.write("Por favor, ingrese un comentario para analizar.")
