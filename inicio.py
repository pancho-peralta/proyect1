import streamlit as st
import pandas as pd
st.title("cris mj")
st.image("https://static.ptocdn.net/images/eventos/pls018_rs.jpg")
st.write("developer pancho")
df = pd.read_csv("https://raw.githubusercontent.com/pancho-peralta/proyect1/refs/heads/main/train.csv")
st.write(df)