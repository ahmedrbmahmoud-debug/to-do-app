import streamlit as st

st.set_page_config(page_title = "school To-Do List", page_icon="📑")

st.title("🧾 School To-Do List App")

    
    
tasks = st.text_area("enter thing that is not in the list and press submit")


#submit
if st.button ("submit"):
    st.checkbox(tasks)
#submit

#subjects
math = st.checkbox("math")
english = st.checkbox("english")
science = st.checkbox("science")
reading = st.checkbox("reading")
computer = st.checkbox("computer")
art = st.checkbox("art")
music = st.checkbox("music")
social_studies = st.checkbox("social studies")
#subject

    
#anmation
if st.button("finsh all tasks"):
    st.balloons()






