from agentmatrix import MultiAgentSystem
import json
import os

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable")

    mas = MultiAgentSystem()
    mas.add_duckduckgo_agent()
    mas.add_llm_agent(
        api_key=api_key,
        model="gpt-4",
        temperature=0.8,
        max_tokens=1000,
        top_p=0.9,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    # Process a query
    conclusion = mas.process_query(
        search_term="current trends in stock and share market",
        expert_type="Financial Market Expert",
        expert_description="You are an expert in the latest trends and developments in the global stock and share market.",
        user_prompt="Provide insights into the current trends and developments in the stock and share market. Include reference links.",
        response_format="json",
        listed_urls=["https://www.marketwatch.com/", "https://www.bloomberg.com/markets"] #which URLs should be referred
    )

    print(json.dumps(conclusion, indent=2))

if __name__ == "__main__":
    main()