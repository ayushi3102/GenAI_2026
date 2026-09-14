import streamlit as st

msz = st.chat_input("Enter you message..")
with st.chat_message("user"):
    st.write("From you :-",msz)
with st.chat_message("assistant"):
    st.write("I am  assistant")
