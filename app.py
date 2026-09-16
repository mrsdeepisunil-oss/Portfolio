import streamlit as st

with open("Portofolio.html", "r") as f:
    html_code = f.read()

st.components.v1.html(html_code, height=1000, scrolling=True)