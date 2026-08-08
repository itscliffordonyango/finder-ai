from app.ai.matcher import calculate_match_score


def rank_job(
    resume_text: str,
    job,
):
    """
    Returns a ranking score between 0 and 100.
    """

    score = calculate_match_score(
        resume_text,
        job.skills or "",
    )

    # Prefer remote jobs
    if job.is_remote:
        score += 5

    # Prefer recent jobs
    score += 2

    return min(score, 100)