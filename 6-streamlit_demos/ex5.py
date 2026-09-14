import streamlit as st

st.success("Login Successful")
st.error("payement failed")
st.warning("ARE U SURE?")
st.info("this site might be dangenrous")

exp = ZeroDivisionError("Divie by zero not allowed!")
st.exception(exp)