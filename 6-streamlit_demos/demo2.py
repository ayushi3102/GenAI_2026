import streamlit as st

if "counter" not in st.session_state :
    st.session_state.counter =0
clicked = st.button("Click Me")
if clicked:
    st.session_state.counter +=1
    
st.write("count is :", st.session_state.counter)

