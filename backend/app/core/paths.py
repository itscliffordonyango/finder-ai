from pathlib import Path

# backend/
BACKEND_DIR = Path(__file__).resolve().parents[2]

UPLOADS_DIR = BACKEND_DIR / "uploads"

RESUME_UPLOAD_DIR = UPLOADS_DIR / "resumes"

RESUME_UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)