from pypdf import PdfReader
def read_pdf(file_path):
    pdf=PdfReader(file_path)
    text = ""
    for i, page in enumerate(pdf.pages):
        content = page.extract_text()
        if content:
            text += content
        return (text)