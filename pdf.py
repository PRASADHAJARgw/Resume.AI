from pypdf import PdfReader

def read_pdf(file_path):
    pdf = PdfReader(file_path)  # file_path can be a file-like object
    text = ""
    for page in pdf.pages:
        content = page.extract_text()
        if content:
            text += content
    return text