import httpx

from bs4 import BeautifulSoup

from app.scrapers.base import BaseScraper


class WeWorkRemotelyScraper(BaseScraper):

    URL = "https://weworkremotely.com/remote-jobs"

    async def scrape(self):

        headers = {
            "User-Agent": "JobFinderAI/1.0",
        }

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.get(
                self.URL,
                headers=headers,
            )

            response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        jobs = []

        articles = soup.select("section.jobs article")

        for article in articles:

            try:

                title = article.select_one(".title")

                company = article.select_one(".company")

                link = article.find("a")

                if not title or not company or not link:
                    continue

                url = (
                    "https://weworkremotely.com"
                    + link["href"]
                )

                jobs.append(
                    {
                        "title": title.text.strip(),
                        "company": company.text.strip(),
                        "location": "Remote",
                        "employment_type": None,
                        "experience_level": None,
                        "description": "",
                        "url": url,
                        "source": "WeWorkRemotely",
                        "salary": None,
                        "skills": None,
                        "is_remote": True,
                    }
                )

            except Exception:
                continue

        return jobs