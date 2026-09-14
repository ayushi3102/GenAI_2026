import streamlit as st

st.title("Main Page")
name = st.sidebar.text_input("Enter your name")
num = st.sidebar.number_input("Enter your age")
st.write("HEllO",name)
st.write("Your age is",num)