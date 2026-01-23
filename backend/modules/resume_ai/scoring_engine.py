def compute_scores(stage1: dict, extracted: dict, gaps: dict):
    # ---------------- FORMAT / ATS ----------------
    ats = round(stage1.get("format_score", 0) * 100, 2)

    # ---------------- SKILLS ----------------
    skill = min(100, len(extracted.get("skills", [])) * 8)

    # ---------------- EXPERIENCE ----------------
    exp = min(100, extracted.get("experience_years", 0) * 20)

    # ---------------- IMPACT (PROJECTS) ----------------
    impact = min(100, len(extracted.get("projects", [])) * 15)

    # ---------------- GAP PENALTY ----------------
    gap_penalty = len(gaps.get("missing_core", [])) * 5

    # ---------------- FINAL SCORE ----------------
    final = max(
        0,
        round((ats + skill + exp + impact) / 4 - gap_penalty, 2)
    )

    # ---------------- RETURN (FRONTEND SAFE) ----------------
    return {
        "ATS_score": ats,
        "Skill_score": skill,
        "Experience_score": exp,
        "Impact_score": impact,
        "Final_score": final
    }
