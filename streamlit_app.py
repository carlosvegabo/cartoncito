import streamlit as st
import requests
from PIL import Image
from io import StringIO
import pandas as pd

with st.container():
  st.subheader("💵 Sube aquí el .csv de tu moxfield y el .txt de las cartas que están buscando")

# Obtener los archivos subidos
uploaded_files = st.file_uploader("Subir archivos", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
  
    # Determinar el tipo de archivo y procesarlo
    if uploaded_file.type == "text/plain":
        text_data = bytes_data.decode("utf-8")
        
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        print(df)
