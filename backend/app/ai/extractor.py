import re

from app.ai.skills import SKILLS

# ==========================================================
# Regular Expressions
# ==========================================================

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PHONE_PATTERN = re.compile(
    r"(\+?\d[\d\s\-]{8,}\d)"
)

LINKEDIN_PATTERN = re.compile(
    r"https?://(?:www\.)?linkedin\.com/[^\s]+",
    re.IGNORECASE,
)

GITHUB_PATTERN = re.compile(
    r"https?://(?:www\.)?github\.com/[^\s]+",
    re.IGNORECASE,
)


# ==========================================================
# Generic Helper
# ==========================================================

def _search(pattern: re.Pattern, text: str) -> str | None:
    """
    Search for the first regex match.

    Returns:
        Matched string or None.
    """

    match = pattern.search(text)

    return match.group() if match else None


# ==========================================================
# Contact Information
# ==========================================================

def extract_email(text: str) -> str | None:
    return _search(EMAIL_PATTERN, text)


def extract_phone(text: str) -> str | None:
    return _search(PHONE_PATTERN, text)


def extract_linkedin(text: str) -> str | None:
    return _search(LINKEDIN_PATTERN, text)


def extract_github(text: str) -> str | None:
    return _search(GITHUB_PATTERN, text)


# ==========================================================
# Personal Information
# ==========================================================

def extract_name(text: str) -> str | None:
    """
    Uses the first non-empty line as the candidate name.

    Later we will replace this with an AI/NER model.
    """

    for line in text.splitlines():

        candidate = line.strip()

        if candidate:
            return candidate

    return None


# ==========================================================
# Skills
# ==========================================================

def extract_skills(text: str) -> list[str]:
    """
    Extract skills from the predefined skills list.
    """

    text_lower = text.lower()

    skills = {
        skill
        for skill in SKILLS
        if skill.lower() in text_lower
    }

    return sorted(skills)


# ==========================================================
# Resume Parser
# ==========================================================

def extract_resume_data(text: str) -> dict:
    """
    Extract all supported information from a resume.
    """

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "github": extract_github(text),
        "linkedin": extract_linkedin(text),
        "skills": extract_skills(text),
    }