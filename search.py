from duckduckgo_search import DDGS

def web_search(query):

    text = ""

    try:
        with DDGS() as ddgs:

            results = list(ddgs.text(query, max_results=5))

        print("\n===== DUCKDUCKGO RESULTS =====")

        for result in results:

            print(result)

            text += f"""
Title: {result.get('title', '')}
Body: {result.get('body', '')}
URL: {result.get('href', '')}

"""

        print("==============================\n")

        if text.strip() == "":
            return "No search results found."

        return text

    except Exception as e:

        print("DuckDuckGo Error:", e)

        return f"Search failed: {e}"