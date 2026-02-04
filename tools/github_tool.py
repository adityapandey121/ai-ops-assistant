import requests


class GitHubTool:
    BASE_URL = "https://api.github.com/search/repositories"

    def search_repositories(self, query: str, top_n: int = 3):
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc"
        }

        response = requests.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        items = response.json().get("items", [])[:top_n]

        results = []
        for repo in items:
            results.append({
                "name": repo["full_name"],
                "stars": repo["stargazers_count"],
                "url": repo["html_url"]
            })

        return results
