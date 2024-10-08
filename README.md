﻿# Análisis de Sentimientos en Comentarios de Redes Sociales

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Streamlit que permite analizar el sentimiento de comentarios en redes sociales como X (anteriormente conocido como Twitter), Facebook, e Instagram. Utiliza el modelo preentrenado de inteligencia artificial de [pysentimiento en español](https://huggingface.co/pysentimiento/robertuito-sentiment-analysis) para clasificar los comentarios en categorías como positivo, negativo o neutral. La aplicación cuenta con una interfaz interactiva y fácil de usar.

## Configuración del Entorno de Desarrollo

### Requisitos Previos

- [Anaconda](https://www.anaconda.com/products/distribution) (para la gestión de entornos)
- Python 3.10

### Procedimiento de Instalación

1. **Clonación del repositorio** en la máquina local:

    ```bash
    git clone https://github.com/Sebastian-Cely/M3-Analisis-de-sentimentos.git
    cd tu_repositorio
    ```

2. **Creación de un entorno virtual en Anaconda** con Python 3.10:

    ```bash
    conda create -n sentiment_analysis python=3.10
    conda activate sentiment_analysis
    ```

3. **Instalación las dependencias** listadas en el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la Aplicación

Para ejecutar la aplicación, seguir los pasos:

1. Verificar el entorno virtual de Anaconda:

    ```bash
    conda activate sentiment_analysis
    ```

2. Ejecutar la aplicación usando Streamlit:

    ```bash
    streamlit run main.py
    ```

Esto iniciará la aplicación web en el navegador. Se puede navegar entre las diferentes páginas de la aplicación utilizando la barra lateral.

## Ejecutar las Pruebas Unitarias

Este proyecto incluye pruebas unitarias para verificar la funcionalidad del análisis de sentimientos. Para ejecutar las pruebas:

1. Verificar el entorno virtual de Anaconda:

    ```bash
    conda activate sentiment_analysis
    ```

2. Ejecutar las pruebas con el siguiente comando:

    ```bash
    python -m unittest discover
    ```

Este comando buscará automáticamente todos los archivos de pruebas en el proyecto y ejecutará las pruebas unitarias.

## Estructura del Proyecto

```
sentiment_analysis_project/
│
├── main.py # Archivo principal para la navegación
├── home.py # Página principal de la aplicación
├── analisis.py # Página de análisis de sentimientos
├── requirements.txt # Archivo de dependencias
├── test_app.py # Pruebas unitarias para la aplicación
└── README.md # Descripción y guía del proyecto
```

