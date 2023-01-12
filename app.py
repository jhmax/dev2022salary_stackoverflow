import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from survey_page import load_survey

page = st.sidebar.selectbox("Explore data", ("Predict", "Explore","Survey Stack overflow 2022"))


if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    load_survey()