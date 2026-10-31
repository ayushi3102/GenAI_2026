import streamlit as st 
import requests

st.set_page_config(page_title='AI Explainer',page_icon = '🤖')
st.title("🤖 AI  Concept Explainer")
st.write('Enter any topic and I will explain  it in simple words for you')

ques= st.text_input("What should I explain ?",placeholder = 'eg. AI, Asynchronous programming')
if st.button('Get Explanaion'): 
    if ques.strip():
        with st.spinner("Generating Explanation..."):
            try:
                ans= requests.post('http://localhost:8000/ask',json = {"question":ques})
                if ans.status_code == 200:
                    data = ans.json()
                    st.success("### AI Response")
                    st.write(data['answer'])
                else:
                    st.error(f"Error : {ans.json().get('detail')}")
            except Exception as ex:
                st.error("Connection failed "+str(ex))
                             
    else:
        st.warning("Please type something first")
