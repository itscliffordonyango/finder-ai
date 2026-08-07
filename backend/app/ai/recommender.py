from app.ai.skills import extract_skills


def generate_recommendation(
    resume_text: str,
    job_skills: str | None,
):
    resume_skills = set(
        extract_skills(resume_text)
    )

    required = set()

    if job_skills:
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

    if missing:
        recommendation = (
            "Improve these skills: "
            + ", ".join(missing[:5])
        )
    else:
        recommendation = (
            "Excellent match."
        )

    return {
        "strengths": strengths,
        "missing_skills": missing,
        "recommendation": recommendation,
    }