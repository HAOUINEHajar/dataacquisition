import streamlit as st
import pandas as pd

def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")
    url = "https://docs.google.com/spreadsheets/d/1KgQ_MTxfQeEqkJi1brg-5hOdqhsshJ9arzCRJcOtvns/edit?gid=0#gid=0"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
show_sheets_page()
