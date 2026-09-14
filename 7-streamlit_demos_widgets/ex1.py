import streamlit as st

course = st.selectbox("Select a course",["--Select --","Py","Java","OS","DBMS"])
if course != "--Select --":
    st.write("YOU selected:",course)



courses = st.multiselect("Select courses",["Py","Java","OS","DBMS","C"],default = "Java")
if courses != []:
    st.write("YOU selected:",courses)