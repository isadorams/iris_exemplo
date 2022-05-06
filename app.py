import streamlit as st
import pickle
from sklearn.preprecessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

st.write("# Classificação de Iris")
st.write("## Exemplo com o comprimento de pétala e sépala")

st.sidebar.write("### Parâmetros")
st.sidebar.slider("Comprimento da sépala", 4.0, 8.0, 5.8, 0.1)
st.sidebar.slider("Comprimento da pétala", 0.9, 7.0, 3.8, 0.1)

with open("objetos.pkl", "rb") as arquivo:
ss, dtc = pickle.load(arquivo)
