import os
import time
import requests

API_KEY = os.getenv("NEWS_API_KEY")
URL = "https://newsapi.org/v2/top-headlines"
VALID_CATEGORIES = {"sports", "technology", "health"}


def get_headlines(category):
    category = category.strip().lower()

    if category not in VALID_CATEGORIES:
        print("Choose one category: sports, technology, or health.")
        return

    if not API_KEY:
        print("API key missing. Set NEWS_API_KEY first.")
        return

    params = {
        "country": "in",
        "category": category,
        "pageSize": 5,
    }
    headers = {"X-Api-Key": API_KEY}

    # Retry once after a short pause if the request fails due to a network error.
    for attempt in range(2):
        try:
            response = requests.get(
                URL, params=params, headers=headers, timeout=10
            )

            if response.status_code == 401:
                print("Invalid or unauthorized NewsAPI key.")
                return
            if response.status_code == 429:
                print("NewsAPI rate limit reached. Try again later.")
                return

            response.raise_for_status()
            data = response.json()

            if data.get("status") != "ok":
                print("NewsAPI error:", data.get("message", "Unknown API error"))
                return

            articles = data.get("articles", [])
            if not articles:
                print("No headlines were found for this category.")
                return

            print(f"\nTop {len(articles)} {category} headlines:\n")
            for number, article in enumerate(articles[:5], start=1):
                title = article.get("title") or "Untitled headline"
                source = (article.get("source") or {}).get("name", "Unknown source")
                print(f"{number}. {title}")
                print(f"   Source: {source}\n")
            return

        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError) as error:
            if attempt == 0:
                print("Request failed. Retrying once...")
                time.sleep(2)
            else:
                print(f"Could not retrieve headlines: {error}")
        except requests.exceptions.HTTPError as error:
            print(f"NewsAPI returned an HTTP error: {error}")
            return
        except ValueError:
            print("NewsAPI returned invalid JSON.")
            return


category = input("Enter category (sports, technology, health): ")
get_headlines(category)