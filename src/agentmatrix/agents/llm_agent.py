from .base_agent import BaseAgent
from openai import OpenAI
import json

class LLMAgent(BaseAgent):
    def __init__(self, api_key, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
        super().__init__()
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.log("LLMAgent initialized")

    def process(self, expert_type, expert_description, user_prompt, response_format, duckduckgo_results):
        self.log(f"Processing request for expert type: {expert_type}")
        system_prompt = f"{expert_type}: {expert_description}"
        full_prompt = (
            f"{system_prompt}\n\n"
            f"User input: {user_prompt}\n\n"
            f"DuckDuckGo results: {json.dumps(duckduckgo_results)}\n\n"
            f"Please provide your response in valid JSON format. Include 'examples' as a list of objects, "
            f"each with 'application', 'description', and 'reference' fields."
        )

        self.log("Sending request to OpenAI API")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )
            self.log("Received response from OpenAI API")
            
            # Attempt to parse the response as JSON
            try:
                self.log("Parsing response as JSON")
                return json.loads(response.choices[0].message.content)
            except json.JSONDecodeError:
                # If parsing fails, return the raw text in a JSON object
                self.log("Failed to parse JSON, returning raw response")
                return json.dumps({"error": "Failed to parse JSON", "raw_response": response.choices[0].message.content})
        
        except Exception as e:
            self.log(f"Error occurred: {str(e)}")
            return json.dumps({"error": str(e)})