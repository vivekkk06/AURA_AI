import re

# ------------------ SKILL DATABASE ------------------

SKILL_DB = [
    "python", "java", "c++", "c", "sql", "fastapi", "flask", "django",
    "docker", "kubernetes", "aws", "azure", "gcp",
    "machine learning", "deep learning", "ai", "ml",
    "nlp", "opencv", "tensorflow", "pytorch",
    "mongodb", "postgresql", "mysql",
    "react", "node", "express", "spring", "git", "linux"
]

# ------------------ PROJECT SECTION EXTRACTOR ------------------

def extract_projects(text: str):
    lines = text.split("\n")
    projects = []
    capture = False

    for line in lines:
        l = line.lower().strip()

        # Start capturing when project section appears
        if any(x in l for x in ["project", "projects", "experience", "internship"]):
            capture = True
            continue

        # Stop when another section starts
        if capture and any(x in l for x in ["education", "skills", "certification", "summary"]):
            break

        if capture and len(line.strip()) > 4:
            projects.append(line.strip())

    return projects[:8]


# ------------------ MAIN EXTRACTION ------------------

def extract_information(text: str):
    text_l = text.lower()

    # ---- SKILLS ----
    skills = sorted({s for s in SKILL_DB if s in text_l})

    # ---- EDUCATION ----
    education = list(set(re.findall(
        r"(b\.tech|m\.tech|bachelor|master|phd|bsc|msc)", text_l
    )))

    # ---- EXPERIENCE YEARS ----
    years = re.findall(r"(\d+(?:\.\d+)?)\s*\+?\s*years", text_l)
    experience_years = float(years[0]) if years else 0.0

    # ---- PROJECTS / WORK ----
    raw_projects = extract_projects(text)

    project_objs = []
    for i, p in enumerate(raw_projects):
        used_tech = [s for s in skills if s in p.lower()]

        project_objs.append({
            "name": f"Project / Work {i+1}",
            "tech": used_tech[:6],
            "impact": p
        })

    return {
        "skills": skills,
        "education": education,
        "experience_years": experience_years,
        "projects": project_objs
    }
