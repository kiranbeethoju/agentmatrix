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

    conclusion = mas.process_query(
        search_term="LLM applications in healthcare",
        expert_type="Healthcare AI Expert",
        expert_description="You are an expert in AI applications in healthcare.",
        user_prompt="Provide examples of LLM applications in healthcare with references.",
        response_format="json",
        listed_urls=["https://www.nature.com/", "https://www.thelancet.com/"]
    )

    print(json.dumps(conclusion, indent=2))

if __name__ == "__main__":
    main()