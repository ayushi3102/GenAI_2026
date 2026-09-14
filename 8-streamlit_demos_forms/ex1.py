import streamlit as st

def handleForm():
    if not st.session_state.username or not st.session_state.age or not st.session_state.sal:
        st.error("All fields required")
    else :
        st.success(f'welcome {st.session_state.username}')
        st.write('name',st.session_state.username,'age',st.session_state.age,'sal',st.session_state.sal)
st.title("LOGIN FORM")
with st.form("login form", clear_on_submit = True):
    name = st.text_input("NAME",key = 'username')
    age = st.number_input("AGE",key = 'age')
    sal = st.number_input("SAL",key = 'sal')
    submitted = st.form_submit_button("Login", on_click = handleForm)

