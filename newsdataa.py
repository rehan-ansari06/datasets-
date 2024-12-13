import requests
import pandas as pd

# Google News API key
api_key = '35d0deb2fab14c229b05b30711044644'

# Base URL for the Google News API
url = 'https://newsapi.org/v2/everything'

# Parameters for the API request
params = {
    'q': 'supply chain',    # Fetch articles containing 'supply chain'
    'language': 'en',       # Fetch articles in English
    'sortBy': 'relevance',  # Sort results by relevance
    'pageSize': 50,         # Fetch up to 50 articles
    'apiKey': api_key       # Your API key
}

# Send the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract articles from the response
    articles = data.get('articles', [])
    if articles:
        # Prepare a list to store article details
        news_list = []
        for article in articles:
            news_list.append({
                'Title': article.get('title'),
                'Description': article.get('description'),
                'URL': article.get('url'),
                'Published At': article.get('publishedAt'),
                'Source': article['source'].get('name') if article.get('source') else 'Unknown'
            })

        # Convert the list to a DataFrame
        news_df = pd.DataFrame(news_list)

        # Save the DataFrame to a CSV file
        csv_file = "supply_chain_news.csv"
        news_df.to_csv(csv_file, index=False)
        print(f"Data has been fetched and saved to {csv_file}")
    else:
        print("No articles found for the query 'supply chain'.")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
