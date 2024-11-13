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
    txt_data = uploaded_txt.readlines()
    st.write("Archivo TXT cargado con éxito")
    #st.text(txt_data)  # Muestra el contenido del archivo TXT

# Guardar los datos en variables para su uso posterior
lines = txt_data

#uwuuwuwuwuwuwuwuuwuwuuwuw apartir de aqui hay logica
# Procesar cada línea para separar en columnas
data = []
for line in lines:
    # Decodificar y limpiar la línea
    line = line.decode("utf-8").strip()
    
    # Separar en dos partes en el primer espacio en blanco encontrado
    parts = line.split(" ", 1)
    
    if len(parts) == 2:
        data.append(parts)
    else:
        data.append([parts[0], ""])

# Crear DataFrame
dftxt = pd.DataFrame(data, columns=["Cantidad", "Carta"])

# Mostrar el DataFrame

with st.container():
  st.subheader("Las cartas que se buscan son:")
  
st.dataframe(dftxt)

#logica para hacer el cruce de información
coincidencias = dftxt['Carta'].isin(csv_data['Name']) 
dftxt['Coincidencias'] = coincidencias
dftxt_filtrado = dftxt[dftxt['Coincidencias'] == True]

with st.container():
  st.subheader("👽Resultado")
  st.text("Las cartas que coinciden son:")

st.dataframe(dftxt_filtrado)

