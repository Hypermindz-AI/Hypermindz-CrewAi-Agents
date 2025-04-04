import os
import requests
from crewai_tools import tool

# Load API key from environment variables
BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")
BROWSERLESS_URL = f"https://chrome.browserless.io/content?token={BROWSERLESS_API_KEY}"

@tool("Browserless HTML Extractor")
def fetch_html(url: str) -> str:
    """Fetches the HTML content of a webpage using Browserless API.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The raw HTML content of the page.
    """
    if not BROWSERLESS_API_KEY:
        return "Error: Browserless API key is missing. Set BROWSERLESS_API_KEY."

    try:
        response = requests.post(
            BROWSERLESS_URL,
            json={"url": url}
        )
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        return f"Error fetching webpage: {str(e)}"
