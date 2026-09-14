import streamlit as st

name = st.text_input("what is your name?",value="guest")

if name :
    st.write("You name is :", name)