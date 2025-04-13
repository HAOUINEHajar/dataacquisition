import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} ! ")
