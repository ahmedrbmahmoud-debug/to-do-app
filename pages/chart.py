import streamlit as st

st.title("The most studied subject in the world")

subjects = ["math","science","language","social studies","computer/ICT"]
st.bar_chart([subjects])