from app.ai.extractor import extract_resume_data


def calculate_ats_score(text: str):
    data = extract_resume_data(text)

    score = 0

    categories = {
        "contact_information": 0,
        "skills": 0,
        "experience": 0,
        "education": 0,
        "projects": 0,
        "formatting": 0,
    }

    feedback = []

    # Contact Information (20)

    if data["email"]:
        categories["contact_information"] += 5

    if data["phone"]:
        categories["contact_information"] += 5

    if data["github"]:
        categories["contact_information"] += 5
        feedback.append("GitHub profile detected.")

    if data["linkedin"]:
        categories["contact_information"] += 5
        feedback.append("LinkedIn profile detected.")

    # Skills (20)

    skill_count = len(data["skills"])

    if skill_count >= 10:
        categories["skills"] = 20

    elif skill_count >= 6:
        categories["skills"] = 16

    elif skill_count >= 3:
        categories["skills"] = 10

    else:
        feedback.append(
            "Add more technical skills."
        )

    # Experience (20)

    if "experience" in text.lower():
        categories["experience"] = 20
    else:
        feedback.append(
            "Experience section missing."
        )

    # Education (15)

    if "education" in text.lower():
        categories["education"] = 15
    else:
        feedback.append(
            "Education section missing."
        )

    # Projects (15)

    if (
        "project" in text.lower()
        or "projects" in text.lower()
    ):
        categories["projects"] = 15
    else:
        feedback.append(
            "Add project experience."
        )

    # Formatting (10)

    if len(text.splitlines()) > 20:
        categories["formatting"] = 10
    else:
        feedback.append(
            "Resume formatting could be improved."
        )

    score = sum(categories.values())

    return {
        "overall_score": score,
        "categories": categories,
        "feedback": feedback,
    }