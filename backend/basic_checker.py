from backend.llm import run_llm
from backend.prompts import BASIC_INFO_PROMPT
from backend.match_score_agent import run_match_score_agent
import json


def basic_checker(job_posting, resume_content, question_count):
    # Basic Information --> Name, Experience, Skils (list)
    # Return Candidate object
    
    match_score = run_match_score_agent(job_posting, resume_content)
    
    llm_response = run_llm(BASIC_INFO_PROMPT, {
        "pdf_text": resume_content,
        "job_posting": job_posting
    })
    
    llm_response = json.loads(llm_response)
    llm_response["matching_score"] = match_score
    return llm_response