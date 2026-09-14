import streamlit as st

name = st.text_input("what is your name?")

if name :
    st.write("You name is :", name)