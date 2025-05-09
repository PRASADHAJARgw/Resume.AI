from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import generate_analysis
## creat the Frontend 
st.header(":blue[Resume Analysis AI] using AI ",divider = "green")
st.subheader("Tips for Using the Application")


## Resume Part

st.sidebar.subheader("Upload the Resume")
resume=st.sidebar.file_uploader(label = "Upload your resume")
a=read_pdf(resume)
notes=f'* **Upload  your resume**:- Please upload your resume. this is GENAI Powered Appilcation. \n\
* **Job Descreption**:- Copy paste. the job Descreption From JOB boards \n\
* **Unlease the pover of AI**:- Click the button to generate the analysis. \n\ '
st.write(notes)

## Job Description Part
st.sidebar.subheader("Enter the Job Description" ,divider = True)
job_decsription = st.text_area(label="Copy paste job descreption ", max_chars=10000)

button = st.button(label="Genreate AI Analysis")
if button:
    st.markdown(generate_analysis(resume_text=a, job_description=job_decsription))
    st.write("Analysis Generated Successfully")

