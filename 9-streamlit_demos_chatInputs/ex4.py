import streamlit as st

st.title("Chat Application")

if "messages"  not in st.session_state : 
    st.session_state.messages =[]


for msz in st.session_state.messages:
    with st.chat_message(msz["role"]):
        st.write(msz['content'])
    

message = st.chat_input("Type your message")

if message:
    st.session_state.messages.append({'role':'user','content':message})
    st.session_state.messages.append({'role':'assistant','content':f"Echo: {message}"})
    st.rerun()




