import streamlit as st

st.title("writing area")
st.write("make sure to press button")
#warning
if st.button("warning"):
  st.error("the text will not be saved")

st.text_area("write anything", height=500)

