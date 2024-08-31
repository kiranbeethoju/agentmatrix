from .base_agent import BaseAgent
import requests
import json

class DuckDuckGoAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.duckduckgo.com/"
        self.log("DuckDuckGoAgent initialized")

    def process(self, search_term, listed_urls=None):
        self.log(f"Processing search term: {search_term}")
        params = {
            'q': search_term,
            'format': 'json'
        }
        self.log("Sending request to DuckDuckGo API")
        response = requests.get(self.base_url, params=params)
        self.log("Received response from DuckDuckGo API")
        results = response.json().get('RelatedTopics', [])
        
        self.log("Filtering and processing results")
        filtered_results = []
        for result in results[:10]:  # Limit to top 10 results
            if 'Text' in result and 'FirstURL' in result:
                if not listed_urls or any(url in result['FirstURL'] for url in listed_urls):
                    filtered_results.append({
                        'text': result['Text'],
                        'url': result['FirstURL']
                    })
        
        self.log(f"Processed {len(filtered_results)} results")
        return filtered_results