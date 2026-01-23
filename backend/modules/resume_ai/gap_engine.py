def compare_resume_vs_role(extracted: dict, role_profile: dict):

    resume_skills = set(extracted.get("skills", []))
    core = set(role_profile.get("core_skills", []))
    tools = set(role_profile.get("tools", []))

    missing_core = list(core - resume_skills)
    weak = list(core & resume_skills) if len(resume_skills) < len(core) else []
    next_level = list(tools - resume_skills)

    return {
        "missing_core": missing_core,
        "weak": weak,
        "next_level": next_level
    }