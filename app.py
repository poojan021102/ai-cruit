import streamlit as st
from io import StringIO
import time
import pdfplumber
from backend.basic_checker import basic_checker

st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
    

vert_space = '<div style="marign-top: 2px 5px;"></div>'
st.markdown(vert_space, unsafe_allow_html=True)
st.title("AI-Cruit")

job_posting = st.text_area(
    "Enter the Job reqirements",
    "",
    height=200,
)

uploaded_file = st.file_uploader("Choose a resume",type=["pdf"],accept_multiple_files=False)
if uploaded_file is not None:
    # To read file as bytes:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    resume_content = text


questions_count = st.number_input("Number of questions per skill",min_value=5, max_value=50)

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        time.sleep(5)
        # Job Posting, Resume Reader -> CheckBasic
        basic_checker(job_posting, resume_content, questions_count)
        st.success("Done!")
        st.switch_page("pages/analysis.py")
        