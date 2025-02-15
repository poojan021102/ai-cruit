BASIC_INFO_PROMPT = """
I'm evaluating the resume of candidate. so your task is to analyze the content of resume that i'm providing you.
Resume : {pdf_text} 
Job requirements: {job_posting}
you have to give response int the following JSON format:
{{
    "name": Name of the candidate,
    "experience": how much experience the candidate has in industry only in years e.g. 1+ year, 2+ years, 3+ years etc.
    "skills": technical skills the candidate has. your response should be like array ["python","c++","java"]
    "summary": analyze the resume and match with job requirements and give summary for why we ahould hire this candidate and if any negative point you found that also mentioned in summary.just give me 3-4 point in summary. bold the important keywords and summary format in array ["point 1", "point 2", ....].
}}

If you not found any of the above information in resume then make it empty "".
your response is only in JSON format not contain any other text.
"""