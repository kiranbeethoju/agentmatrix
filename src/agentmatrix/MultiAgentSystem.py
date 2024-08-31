from .agents import DuckDuckGoAgent, LLMAgent

class MultiAgentSystem:
    def __init__(self):
        self.duckduckgo_agents = []
        self.llm_agents = []

    def add_duckduckgo_agent(self):
        self.duckduckgo_agents.append(DuckDuckGoAgent())

    def add_llm_agent(self, api_key, model="gpt-3.5-turbo", temperature=0.7, max_tokens=None, top_p=1, frequency_penalty=0, presence_penalty=0):
        self.llm_agents.append(LLMAgent(api_key, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty))

    def process_query(self, search_term, expert_type, expert_description, user_prompt, response_format, listed_urls=None):
        duckduckgo_results = []
        for agent in self.duckduckgo_agents:
            duckduckgo_results.extend(agent.process(search_term, listed_urls))

        llm_results = []
        for agent in self.llm_agents:
            llm_results.append(agent.process(expert_type, expert_description, user_prompt, response_format, duckduckgo_results))

        return llm_results[0] if llm_results else json.dumps({"error": "No LLM agent results"})