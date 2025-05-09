import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_analysis(resume_text, job_description):
    if resume_text is not None:
       st.markdown("Resume Uploated Successfully")
    else:
        st.warning("Please upload a resume.")
    prompt = f"""
    You are an AI assistant that analyzes resumes and job descriptions. 
    Your task is to provide a detailed analysis of the resume in relation to the job description.
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Please provide a comprehensive analysis, including strengths, weaknesses, and suggestions for improvement.
    """
    response = model.generate_content(prompt)
    return (st.write(response.text,resume_text,job_description))
