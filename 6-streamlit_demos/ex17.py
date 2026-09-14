import streamlit as st
name = st.text_input("What is your name ?")
age = st.number_input("What is your age ?")
if name :
    st.session_state.username = name
if age:
    st.session_state.age = age
if "username" in st.session_state :
    st.write("Hello",st.session_state.username)