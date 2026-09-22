import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate.from_template("""
Welcome to AI powered tips generator.
Your company name  is {company_name}.
You are applying for {position}.
Based on your strengths {strength} and weakness {weakness}, suggest five  tips.
""")
llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash"
        )

st.title("AI powered tips generator")
company_name = st.text_input("Enter your company name")
position = st.text_input("Title you are applying for ")
strength = st.text_input("Enter your strengths")
weakness = st.text_input("Enter your weakness")

if company_name and position and strength and weakness:
    formatted_prompt = prompt.format(
            company_name=company_name,
            position=position,
            strength=strength,
            weakness=weakness
        )
    st.write(formatted_prompt)
    res = llm.invoke(formatted_prompt)
    st.write(res.content)
