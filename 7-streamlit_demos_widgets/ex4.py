import streamlit as st

file = st.file_uploader("Upload an image", type =["jpg","png"])
if file:
    st.success("Image uploaded")
    st.image(file)
