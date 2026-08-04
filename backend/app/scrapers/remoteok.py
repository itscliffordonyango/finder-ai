import httpx

from app.scrapers.base import BaseScraper


class RemoteOKScraper(BaseScraper):

    API_URL = "https://remoteok.com/api"

    async def scrape(self) -> list[dict]:

        headers = {
            "User-Agent": "JobFinderAI/1.0"
        }

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.get(
                self.API_URL,
                headers=headers,
            )

            response.raise_for_status()

            data = response.json()

        jobs = []

        for item in data:

            if not isinstance(item, dict):
                continue

            if not item.get("position"):
                continue

            jobs.append(
                {
                    "title": item.get("position"),
                    "company": item.get("company"),
                    "location": item.get("location") or "Remote",
                    "employment_type": None,
                    "experience_level": None,
                    "description": item.get("description") or "",
                    "url": item.get("url"),
                    "source": "RemoteOK",
                    "salary": (
                        str(item["salary_min"])
                        if item.get("salary_min")
                        else None
                    ),
                    "skills": ", ".join(
                        item.get("tags", [])
                    ),
                    "is_remote": True,
                }
            )

        return jobs