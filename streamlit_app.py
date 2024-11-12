import streamlit as st
import requests
from PIL import Image
from io import StringIO
import pandas as pd

with st.container():
  st.subheader("💵 Sube aquí el .csv de tu moxfield")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dfcsv = pd.read_csv(uploaded_file)

with st.container():
  st.subheader("🔍 Sube aquí el .txt de las cartas que están buscando ")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data2 = uploaded_file.getvalue()
    st.write(bytes_data2)

    # To convert to a string based IO:
    stringio2 = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio2)

    # To read file as string:
    string_data2 = stringio.read()
    st.write(string_data2)

    # Can be used wherever a "file-like" object is accepted:
    dftxt = pd.read_csv(uploaded_file)
