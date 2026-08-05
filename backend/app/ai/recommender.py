from app.ai.extractor import extract_skills


def generate_recommendation(
    resume_text: str,
    job_skills: str | None,
):
    """
    Compare resume skills against job skills and
    generate an explanation.
    """

    if not job_skills:
        return {
            "strengths": [],
            "missing_skills": [],
            "recommendation": "No skills listed for this job.",
        }

    resume_skills = set(
        extract_skills(resume_text)
    )

    required = {
        skill.strip()
        for skill in job_skills.split(",")
        if skill.strip()
    }

    strengths = sorted(
        resume_skills & required
    )

    missing = sorted(
        required - resume_skills
    )

    if not missing:
        recommendation = (
            "Excellent match. Apply immediately."
        )

    elif len(missing) <= 2:
        recommendation = (
            "Good match. Learning the missing skills could significantly improve your chances."
        )

    else:
        recommendation = (
            "Moderate match. Consider strengthening the missing skills before applying."
        )

    return {
        "strengths": strengths,
        "missing_skills": missing,
        "recommendation": recommendation,
    }