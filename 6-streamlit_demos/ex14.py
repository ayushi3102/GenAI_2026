import streamlit as st

num = st.text_input("what is your aadhar no. ?",max_chars = 6 )

if num :
    st.write("You adhar no is :", num)