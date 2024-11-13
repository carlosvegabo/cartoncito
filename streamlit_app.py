import streamlit as st
import requests
from PIL import Image
from io import StringIO
import pandas as pd

with st.container():
  st.subheader("💵 Sube aquí el .csv de tu moxfield")

# Subir archivo .csv
uploaded_csv = st.file_uploader("Sube un archivo CSV", type="csv")

with st.container():
  st.subheader("🔍 Sube aquí el .txt de las cartas que están buscando")

# Subir archivo .txt
uploaded_txt = st.file_uploader("Sube un archivo TXT", type="txt")

# Variable para almacenar los datos cargados
csv_data = None
txt_data = None

# Procesar archivo CSV
if uploaded_csv is not None:
    # Leer el archivo CSV en un DataFrame de pandas
    csv_data = pd.read_csv(uploaded_csv)
    st.write("Archivo CSV cargado con éxito")

# Procesar archivo TXT
if uploaded_txt is not None:
    # Leer el archivo TXT como texto
    txt_data = uploaded_txt.read().splitlines()
    st.write("Archivo TXT cargado con éxito")
    st.text(txt_data)  # Muestra el contenido del archivo TXT

# Guardar los datos en variables para su uso posterior
archivo_csv = csv_data
archivo_txt = txt_data

#uwuuwuwuwuwuwuwu
split_palabras = [linea.split(None, 1) for linea in txt_data]
