from backend.llm import run_llm
from backend.prompts import BASIC_INFO_PROMPT

def basic_checker(job_posting, resume_content, question_count):
    # Basic Information --> Name, Experience, Skils (list)
    # Return Candidate object
    llm_response = run_llm(BASIC_INFO_PROMPT, {
        "pdf_text": resume_content
    })
    print(llm_response)