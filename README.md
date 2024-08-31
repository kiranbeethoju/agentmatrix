# README.md
# agentmatrix Package

A Python package that implements agentmatrix a multi-agent system for processing queries using DuckDuckGo and LLM agents.

## Installation

```bash
pip install agentmatrix
```

## Usage

```python
from agentmatrix import MultiAgentSystem

# Initialize the system
mas = MultiAgentSystem()

# Add agents
mas.add_duckduckgo_agent()
mas.add_llm_agent(api_key="your-api-key", model="gpt-4")

# Process a query
result = mas.process_query(
    search_term="Your search term",
    expert_type="Expert type",
    expert_description="Expert description",
    user_prompt="Your prompt",
    response_format="json",
    listed_urls=["https://example.com"]
)

print(result)
```

## License

This project is licensed under the MIT License.

# requirements.txt
requests==2.26.0
openai==0.27.0

# .gitignore
__pycache__/
*.py[cod]
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.env
