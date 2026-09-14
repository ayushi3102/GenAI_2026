import streamlit as st

num1 = st.number_input("Enter your first no :",key = 1)
num2 = st.number_input("Enter your second no :",key = 2)
is_clicked = st.button("Add")

if is_clicked:
   st.write(f"Your total sum is {num1+num2}")

