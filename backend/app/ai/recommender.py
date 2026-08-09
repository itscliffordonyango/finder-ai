from app.ai.skills import extract_skills


def generate_recommendation(
    resume_text: str,
    job_skills: str | None,
):
    resume_skills = {
        skill.lower()
        for skill in extract_skills(resume_text)
    }

    required_skills = set()

    if job_skills:
        required_skills = {
            skill.strip().lower()
            for skill in job_skills.split(",")
            if skill.strip()
        }

    matched_skills = sorted(
        resume_skills & required_skills
    )

    missing_skills = sorted(
        required_skills - resume_skills
    )

    total_required = len(required_skills)
    total_matched = len(matched_skills)

    if total_required:
        score = round(
            (total_matched / total_required) * 100,
            2,
        )
    else:
        score = 0.0

    if score >= 80:
        recommendation = "Excellent match"
        priority = "high"

    elif score >= 60:
        recommendation = "Strong match"
        priority = "medium"

    elif score >= 40:
        recommendation = "Potential match"
        priority = "low"

    else:
        recommendation = "Weak match"
        priority = "low"

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation,
        "priority": priority,
    }

