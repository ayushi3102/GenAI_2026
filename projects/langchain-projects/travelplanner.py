import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


def format_prompt(city, month, language, budget):
    prompt = PromptTemplate.from_template(
        """ 
Welcome to the {city} travel guide.
If you are visiting in {month} here's what you can do :
1. Must visit attractions
2. Local cusuine you must try 
3. Useful phrases in {language}
4. Tips for travelling on a budget {budget}
Enjoy you trip. 
        """
        
    )

    formatted_prompt = prompt.format(
        city=city,
        month=month,
        language=language,
        budget=budget
    )

    st.write(formatted_prompt)
    return formatted_prompt


def ai_result(formatted_prompt):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    res = llm.invoke(formatted_prompt)

    st.write(res.content)


def handleForm(city, month, language, budget):
    if not city or not month or not language:
        st.error("All fields required")

    elif budget == "--Select --":
        st.error("Select your budget first")

    else:
        formatted_prompt = format_prompt(
            city,
            month,
            language,
            budget
        )

        ai_result(formatted_prompt)


st.title("Travel Guide")

with st.form("Travel Guide", clear_on_submit=True):

    city = st.text_input("Enter your city")
    month = st.text_input("Enter the month of travel")
    language = st.text_input("Enter the language")

    budget = st.selectbox(
        "Select your budget",
        ["--Select --", "Low", "Medium", "High"]
    )

    submitted = st.form_submit_button("Submit")

    if submitted:
        handleForm(city, month, language, budget)
