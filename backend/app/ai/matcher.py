from app.ai.extractor import extract_skills


def calculate_match_score(
    resume_text: str,
    job_skills: str | None,
) -> float:
    """
    Compare resume skills against job skills.

    Returns:
        float between 0 and 100
    """

    if not job_skills:
        return 0.0

    resume_skills = set(
        extract_skills(resume_text)
    )

    required_skills = {
        skill.strip()
        for skill in job_skills.split(",")
        if skill.strip()
    }

    if not required_skills:
        return 0.0

    matched = resume_skills & required_skills

    score = (
        len(matched)
        / len(required_skills)
    ) * 100

    return round(score, 2)