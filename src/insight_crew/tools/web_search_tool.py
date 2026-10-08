import os
from dotenv import load_dotenv
from tavily import TavilyClient
from crewai.tools import tool

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=tavily_api_key)


@tool("Web Search Tool")
def web_search_tool(query: str) -> str:
    """
    Search the internet for current and relevant information.
    Use this tool when the user asks about recent events,
    current market information, statistics, companies,
    competitors, technologies, or any topic requiring
    up-to-date information.
    """

    try:
        response = tavily_client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return "No relevant search results were found."

        formatted_results = []

        for result in results:
            title = result.get("title", "")
            content = result.get("content", "")
            url = result.get("url", "")

            formatted_results.append(
                f"Title: {title}\n"
                f"Content: {content}\n"
                f"Source: {url}\n"
            )

        return "\n---\n".join(formatted_results)

    except Exception as e:
        return f"Web search failed: {str(e)}"