from backend.llm import run_llm
from backend.prompts import BASIC_INFO_PROMPT
import json

def basic_checker(job_posting, resume_content, question_count):
    # Basic Information --> Name, Experience, Skils (list)
    # Return Candidate object
    llm_response = run_llm(BASIC_INFO_PROMPT, {
        "pdf_text": resume_content
    })
    llm_response = json.loads(llm_response)
    return llm_response