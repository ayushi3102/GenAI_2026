import streamlit as st

addres = st.text_area("your address?",placeholder="xyz",height = 300)

if addres :
    st.write("You address is :", )
    st.write(addres)


age = st.number_input("Enter your age",min_value=0,max_value= 80,step=4)
if age:
    st.write("Your age is:",age)