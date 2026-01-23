from PyPDF2 import PdfReader


def read_pdf(file):
    reader = PdfReader(file)
    return "\n".join([p.extract_text() for p in reader.pages])
