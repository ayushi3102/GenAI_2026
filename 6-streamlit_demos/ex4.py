import streamlit as st

st.markdown("<h3>Way to convert html </h3>")                                # as it is will print
st.markdown("<h3 style ='color:green' >Way to convert html </h3>", unsafe_allow_html = True)   # this unsafe_allow_html help to convert html,by default its value is False

