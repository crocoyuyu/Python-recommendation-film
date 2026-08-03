import streamlit as st

st.title("Système de recommandation dpython -m streamlit run app.pye films")

st.write("Streamlit fonctionne correctement !")

film = st.text_input("Entre le nom d'un film que tu aimes")

if film:
    st.success(f"Nous chercherons des films similaires à : {film}")