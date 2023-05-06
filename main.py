import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=500)

with col2:
    st.title("Muddassar Hussain")
    text = """
    I am Electronic Engineer by education and Python developer by Profession. 
    i am working myself on different projects for my practice and ,
    i have created todo app, 
    A Webcam reader app that will access your web cam and take photo by clicking and convert it into a gray scale photo.
    """
    st.info(text)