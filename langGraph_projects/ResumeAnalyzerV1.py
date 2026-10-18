
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document

load_dotenv()

# Step 1: State
class State(TypedDict):
    resume: str
    analysis: str
    feedback: str
    count: int


# Step 2: LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# Step 3: Nodes
def analyze_resume(state: State):
    prompt = f"""
    Analyze the following resume and provide detailed improvement suggestions.
    Focus on:
    - Skills
    - Projects
    - Experience
    - Structure
    - Impact

    Resume:
    {state['resume']}

    Give at least 5 strong actionable suggestions.
    """

    if state['feedback'] and state['feedback'] != 'good':
        prompt += f"\nPrevious feedback: {state['feedback']}"
        prompt += "\nImprove your previous analysis based on this feedback."

    response = llm.invoke(prompt)

    return {
        'analysis': response.content,
        'count': state['count'] + 1
    }


def review_analysis(state: State):
    text = state['analysis']

    if len(text) < 200:
        return {'feedback': 'Too short. Add more details.'}

    if 'skills' not in text.lower():
        return {'feedback': 'Skills missing. Add skills too.'}

    return {'feedback': 'good'}


def should_continue(state: State):
    if state['feedback'] == 'good' or state['count'] >= 3:
        return 'end'

    return 'retry'


# Step 4: Graph
builder = StateGraph(State)

builder.add_node("analyze", analyze_resume)
builder.add_node("review", review_analysis)

builder.add_edge(START, "analyze")
builder.add_edge("analyze", "review")

builder.add_conditional_edges(
    "review",
    should_continue,
    {
        "end": END,
        "retry": "analyze"
    }
)

# Step 5: Compile
graph = builder.compile()


# Step 6: Streamlit UI
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="centered"
)

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF, Word, TXT)",
    type=["pdf", "docx", "txt"]
)

resume_text = ""

if uploaded_file is not None:
    try:
        if uploaded_file.name.lower().endswith(".pdf"):
            reader = PdfReader(uploaded_file)
            resume_text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        elif uploaded_file.name.lower().endswith(".docx"):
            doc = Document(uploaded_file)
            resume_text = "\n".join(
                para.text for para in doc.paragraphs
            )

        elif uploaded_file.name.lower().endswith(".txt"):
            resume_text = uploaded_file.getvalue().decode("utf-8")

        if resume_text.strip():
            st.success("Resume uploaded successfully!")
        else:
            st.warning(
                "No text found. The PDF may be scanned or image-based."
            )

    except Exception as e:
        st.error(f"Could not read the uploaded file: {e}")


if st.button("Analyze Resume"):
    if not resume_text.strip():
        st.warning("Please upload a readable resume first.")

    else:
        with st.spinner("Analyzing resume..."):
            try:
                result = graph.invoke({
                    "resume": resume_text,
                    "analysis": "",
                    "feedback": "",
                    "count": 0
                })

                st.success("Analysis complete!")
                st.subheader("Suggestions")
                st.write(result["analysis"])

                st.subheader("Attempts Used")
                st.write(result["count"])

            except Exception as e:
                st.error(f"Analysis failed: {e}")
