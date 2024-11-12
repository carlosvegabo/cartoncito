import streamlit as st
import requests
from PIL import Image
from io import StringIO
import pandas as pd

with st.container():
  st.subheader("💵 Sube aquí el .csv de tu moxfield")

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    dataframe = pd.read_csv(uploaded_files.name)

with st.container():
  st.subheader("💵 Sube aquí el .txt de las cartas que están buscando")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")
