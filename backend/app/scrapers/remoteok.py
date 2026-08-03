import httpx

from app.scrapers.base import BaseScraper


class RemoteOKScraper(BaseScraper):

    API_URL = "https://remoteok.com/api"

    async def scrape(self) -> list[dict]:

        headers = {
            "User-Agent": "JobFinderAI/1.0",
        }

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.get(
                self.API_URL,
                headers=headers,
            )

            response.raise_for_status()

            jobs = response.json()

        results = []

        for job in jobs:

            # First item is metadata
            if not isinstance(job, dict):
                continue

            if "position" not in job:
                continue

            results.append(
                {
                    "title": job.get("position"),
                    "company": job.get("company"),
                    "location": job.get("location") or "Remote",
                    "employment_type": None,
                    "experience_level": None,
                    "description": job.get("description") or "",
                    "url": job.get("url"),
                    "source": "RemoteOK",
                    "salary": job.get("salary_min"),
                    "skills": ", ".join(job.get("tags", [])),
                    "is_remote": True,
                }
            )

        return results