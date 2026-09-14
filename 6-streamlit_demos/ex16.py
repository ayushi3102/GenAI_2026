import streamlit as st

clicked = st.button("Click me")
if clicked:
    st.write('you just clicked')