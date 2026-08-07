import re

SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "C",
    "C++",
    "C#",
    "Go",
    "Rust",
    "PHP",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "SQLite",
    "Redis",
    "Docker",
    "Kubernetes",
    "Linux",
    "Git",
    "GitHub",
    "FastAPI",
    "Flask",
    "Django",
    "React",
    "Next.js",
    "Angular",
    "Vue",
    "Node.js",
    "Express",
    "AWS",
    "Azure",
    "GCP",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn",
]


def extract_skills(text: str) -> list[str]:
    """
    Extract known skills from text.
    """

    if not text:
        return []

    text_lower = text.lower()

    found = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found.append(skill)

    return sorted(set(found))