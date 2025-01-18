import requests
from bs4 import BeautifulSoup

def fetch_and_parse_results():
    url = "https://nihongotools.com/?s=%E8%B5%B7%E7%AB%8B&post_type=example-sentence"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Fetch the page
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Failed to fetch page. Status code: {response.status_code}"

        # Parse the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize the results list
        result_list = []

        # Find all .search-result-item elements
        for item in soup.select(".search-result-item"):
            # Extract contents of sub-elements
            romaji = item.select_one(".search-result-romaji")
            title = item.select_one(".search-result-title")
            english = item.select_one(".search-result-english")

            # Create a dictionary with extracted values
            result_dict = {
                "romaji": romaji.get_text(strip=True) if romaji else None,
                "title": title.get_text(strip=True) if title else None,
                "english": english.get_text(strip=True) if english else None,
            }

            # Add the dictionary to the results list
            result_list.append(result_dict)

        return result_list

    except Exception as e:
        return f"An error occurred: {e}"

# Execute the function and print the results
parsed_results = fetch_and_parse_results()
for result in parsed_results:
    print(result)
