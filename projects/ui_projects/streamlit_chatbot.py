import streamlit as st
from dotenv import  load_dotenv
import json
import os
from openai import OpenAI
import time
from datetime import datetime

CHAT_DIR ='chats'

def get_openai_client():
    load_dotenv()
    return OpenAI()


       


ai_client = get_openai_client()
os.makedirs(CHAT_DIR,exist_ok=True)

def new_chat():
    chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(CHAT_DIR,f"{chat_id}.json")
    messages = [{
            'role':'system',
            'content':(
                'You are a PyMentor, a python tutor'
                'Answer only question related to python programming.'
                'for any other question politely refuse'
                )
            }]
    save_chat_history(file_path,messages)
    return chat_id

def save_chat_history(path,messages):
    with open(path,"w") as f:
        json.dump(messages,f,indent=4)

def load_chat_history(path):
        with open(path,"r") as f:
            return json.load(f)
    

def list_chats():
    file_list = os.listdir(CHAT_DIR)  
    sorted_list = sorted(file_list,reverse=True)
    return sorted_list


def stream_chat_with_ai(message,model,temperature):
    placeholder = st.empty()
    stream = ai_client.responses.create(
        model = model,
        input = message,
        stream=True,
        temperature=temperature)
    full_response = ""
    for event in stream:
        if event.type == 'response.output_text.delta':
            token = event.delta
            full_response +=token
            placeholder.markdown(full_response)
    return full_response



st.set_page_config(page_title = "PyMentor", layout = "centered")
st.title("PyMentor  - Python Tuto Chatbot ")
st.write("Welcome to your AI powered Python Assistant")
st.caption("Multiple Chats | Streaming | Resume Chat | Controls Enabled ")

st.sidebar.header("Chat Settings")

if "current_chat" not in st.session_state:
    st.session_state.current_chat = new_chat()

sel_index = list_chats().index(f"{st.session_state.current_chat}").json
selected_chat = st.sidebar.selectbox('Select Chat',list_chats(),index = sel_index)

if selected_chat.replace('.json','') != st.session_state.current_chat :
    st.session_state.current_chat = selected_chat.replace('.json','')
    st.rerun()

if st.sidebar.button("New Chat") :
    st.session_state.current_chat = new_chat()
    st.rerun()




model = st.sidebar.selectbox('Choose Model',['gpt-5.1','gpt-4o-mini'])
temperature = st.sidebar.slider("Temperature", 0.0,  2.0,0.7)
chat_path = os.path.join(CHAT_DIR,f'{st.session_state.current_chat}.json')

messages = load_chat_history(chat_path)


# if "messages" not in  st.session_state :
#     st.session_state.messages = load_chat_history()

message_count = len([m for m in messages if m['role']!='system'])

st.sidebar.metric("Message",message_count)

for msg in messages :
    if msg['role'] != 'system':
        st.chat_message(msg['role']).markdown(msg['content'])

with st.form("chat_app",clear_on_submit =True):
    user_input = st.text_area("Ask a python question:",height = 100,placeholder = "eg. Explain list in python ")
    submit = st.form_submit_button("Ask PyMentor")

if submit and user_input.strip():
    
        st.chat_message('user').markdown(user_input)
        messages.append({"role":"user","content":user_input})
        with st.chat_message('assistant'):
            typing = st.empty()
            typing.markdown("PyMentor is typing...")
            time.sleep(0.5)
            ai_reply = stream_chat_with_ai(messages,model,temperature)
            typing.write("")
        
        messages.append({"role":"assistant","content":ai_reply})
        save_chat_history(chat_path,messages)
        st.rerun()

if st.sidebar.button("Delete Chat:"):
    os.remove(chat_path)
    st.session_state.current_chat = new_chat()
    st.rerun()

