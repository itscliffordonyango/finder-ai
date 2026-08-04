from app.ai.extractor import extract_resume_data
from app.ai.skills import SKILLS


def analyze_resume(
    resume_text: str,
    job_skills: str,
):
    """
    Analyze a resume against a job's required skills.
    """

    data = extract_resume_data(resume_text)

    resume_skills = set(data["skills"])

    required_skills = {
        skill.strip()
        for skill in job_skills.split(",")
        if skill.strip()
    }

    matched = sorted(
        resume_skills & required_skills
    )

    missing = sorted(
        required_skills - resume_skills
    )

    strengths = []

    if data["github"]:
        strengths.append("GitHub profile detected")

    if data["linkedin"]:
        strengths.append("LinkedIn profile detected")

    if resume_skills:
        strengths.append(
            f"{len(resume_skills)} technical skills detected"
        )

    score = 0

    if required_skills:
        score = round(
            len(matched)
            / len(required_skills)
            * 100,
            1,
        )

    recommendation = (
        "Excellent match."
        if score >= 80
        else f"Learn {', '.join(missing[:3])} to improve your chances."
    )

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "strengths": strengths,
        "recommendation": recommendation,
    }