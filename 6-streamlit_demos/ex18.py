import streamlit as st
name = st.text_input("What is your name ?",key = "username")
if  st.session_state.username != "" :
    st.write("Hello",st.session_state.username)