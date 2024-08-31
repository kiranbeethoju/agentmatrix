# test.py
from agentmatrix import MultiAgentSystem
import json

def get_api_key():
    return "your open ai"

def main():
    api_key = get_api_key()
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

    conclusion = mas.process_query(
        search_term="LLM based applications deployed in production usa healthcare",
        expert_type="Healthcare LLM Expert",
        expert_description="You are an expert in real-world usage of generative AI and LLMs in production in USA healthcare.",
        user_prompt="Provide real-world examples of generative AI and LLM applications in production in USA healthcare. Include reference links.",
        response_format="json",
        listed_urls=["https://analyticsindiamag.com/", "https://www.alpha-sense.com/"]
    )

    # Handle both string and dictionary responses
    if isinstance(conclusion, str):
        try:
            conclusion_dict = json.loads(conclusion)
        except json.JSONDecodeError:
            conclusion_dict = {"error": "Failed to parse JSON", "raw_response": conclusion}
    else:
        conclusion_dict = conclusion

    # Pretty print the JSON response
    print(json.dumps(conclusion_dict, indent=2))

if __name__ == "__main__":
    main()