import re
from langchain_community.document_loaders import PyPDFLoader


def parse_resume_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    raw_text = "\n".join([d.page_content for d in docs])

    sections = re.findall(
        r"(Education|Skills|Projects|Experience|Certifications|Internship|Summary)",
        raw_text,
        re.IGNORECASE
    )

    format_score = min(1.0, 0.4 + (len(set(sections)) * 0.1))

    return {
        "raw_text": raw_text,
        "sections": list(set(sections)),
        "format_score": round(format_score, 2)
    }
