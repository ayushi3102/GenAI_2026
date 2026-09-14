import streamlit as st

gen = st.radio("Select gender",["Male","Female","Other"])

st.write("Gender",gen)

agree = st.checkbox("I agree to the terms")
if agree:
    st.info("Thanks for agreeing")
