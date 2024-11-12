import streamlit as st
import requests
from PIL import Image
from io import StringIO
import pandas as pd

with st.container():
  st.subheader("💵 Sube aquí el .csv de tu moxfield y el .txt de las cartas que están buscando")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    
    # To read file as string:
    string_data = stringio.read()
    
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
