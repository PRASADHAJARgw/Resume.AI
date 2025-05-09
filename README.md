<!-- # Resume.AI

Here i am building an Ai application that can analyse resume vs job descreption and daraw insights

- Files that intent to create are app.py with another file `acalysis.py` that can have the prompts and genAi.
  model folled by `PDF.py` which will capture the pdf file and extracr resume text
- `.env` to store the gemeini api key
- `requirements.txt` to store the liabrarys. -->
# 📄 Resume.AI

**Resume.AI** is an AI-powered application that analyzes a candidate's resume against a job description and provides deep insights for HR professionals, including:

- Job fit assessment
- Selection probability
- Resume improvement suggestions
- Technical & HR interview questions
- Career preparation advice

---

## 🚀 Features

- Upload or paste resume and job description
- Gemini AI-powered deep analysis
- LinkedIn and psychometric support (optional)
- Clean Streamlit UI for recruiters and hiring managers

---

## 📁 Project Structure
Resume.AI/
│
├── app.py              # Streamlit frontend
├── analysis.py         # Contains prompt logic and Gemini interaction
├── PDF.py              # Extracts text from uploaded PDF resumes
├── .env                # Environment variables (e.g., GEMINI_API_KEY)
├── requirements.txt    # Python dependencies
└── README.md           # Project overview and setup


## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Resume.AI.git
cd Resume.AI

Create and activate virtual environment

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

GEMINI_API_KEY=your_gemini_api_key_here


streamlit run app.py

streamlit
google-generativeai
python-dotenv
PyPDF2