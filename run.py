import streamlit as st
from stations import run_app
from analyse import run_analyse

page = st.sidebar.radio("Menu", ["Home", "Stations info", "Station analyse"])


if page == "Home":
    st.write("Vitej")
elif page == "Stations info":
    run_app()
else:
    run_analyse()