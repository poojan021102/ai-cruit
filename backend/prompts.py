BASIC_INFO_PROMPT = """
I'm evaluating the resume of candidate. so your task is to analyze the content of resume that i'm providing you.
Resume : {pdf_text} 
you have to give response int the following JSON format:
{{
    "name": Name of the candidate,
    "experience": how much experience the candidate has in industry only in years,
    "skills": technical skills the candidate has. your response should be like array ["python","c++","java"],
}}

If you not found any of the above information in resume then make it empty "".
your response is only in JSON format not contain any other text.
"""