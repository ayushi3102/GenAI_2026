import streamlit as st

page = st.sidebar.radio("Go to",["Home","Profile","Settings"])
if page == "Settings":
    st.title("Settings")
    st.write("Adjust your settings here")
elif page == "Profile":
    st.title("Profile")
    st.write("Adjust your Profile settings here")
elif page == "Home":
    st.title("Home")
    st.write("Adjust your Home settings here")