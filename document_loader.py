from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(file):

    doc = Document(file)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return "Unsupported file format"