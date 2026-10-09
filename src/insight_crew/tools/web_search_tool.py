
import os
import re
from urllib.parse import urlparse

from dotenv import load_dotenv
from tavily import TavilyClient
from crewai.tools import tool

load_dotenv()


@tool("Advanced Web Research Tool")
def web_search_tool(query: str) -> str:
    """
    Search the web for current and relevant research information.

    Provide one query or multiple search queries separated by
    new lines or semicolons. Up to four queries are searched.
    Results are deduplicated by URL and returned with titles,
    source URLs, and available content.
    """

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return (
            "Web search unavailable: TAVILY_API_KEY is missing. "
            "Add it to the project's .env file."
        )

    # Accept multiple queries in one tool call.
    queries = [
        item.strip()
        for item in re.split(r"[\n;]+", query)
        if item.strip()
    ]

    # Keep the tool call bounded.
    queries = queries[:4]

    if not queries:
        return "Please provide at least one search query."

    try:
        client = TavilyClient(api_key=api_key)

        collected_results = []
        seen_urls = set()

        for search_query in queries:
            response = client.search(
                query=search_query,
                search_depth="advanced",
                max_results=5
            )

            for result in response.get("results", []):
                title = (result.get("title") or "").strip()
                content = (result.get("content") or "").strip()
                url = (result.get("url") or "").strip()

                if not url or not content:
                    continue

                # Normalize URLs to avoid simple duplicates.
                normalized_url = urlparse(url)._replace(
                    query="",
                    fragment=""
                ).geturl().rstrip("/").lower()

                if normalized_url in seen_urls:
                    continue

                seen_urls.add(normalized_url)

                collected_results.append({
                    "query": search_query,
                    "title": title or "Untitled source",
                    "content": content[:2500],
                    "url": url
                })

        if not collected_results:
            return "No usable search results were found."

        output = [
            "WEB RESEARCH RESULTS",
            f"Queries searched: {len(queries)}",
            f"Unique sources found: {len(collected_results)}",
            "",
            "Important: Search results are evidence to evaluate, "
            "not automatically verified facts.",
            ""
        ]

        for index, result in enumerate(collected_results, start=1):
            output.append(
                f"SOURCE {index}\n"
                f"Search query: {result['query']}\n"
                f"Title: {result['title']}\n"
                f"Content: {result['content']}\n"
                f"URL: {result['url']}\n"
                f"{'-' * 60}"
            )

        return "\n".join(output)

    except Exception as error:
        return f"Web search failed: {type(error).__name__}: {error}"