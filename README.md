# AgentMatrix

AgentMatrix is an open-source framework for building and orchestrating AI agents. It provides a flexible and extensible architecture for creating, managing, and interacting with various types of AI agents, including language models and search engines.

## Features

- Modular agent architecture
- Easy integration with DuckDuckGo for web searches
- Seamless interaction with OpenAI's language models
- Extensible base classes for creating custom agents
- Logging system for transparency and debugging

## Installation

Install AgentMatrix using pip:

```bash
pip install agentmatrix
```

## Quick Start

Here's a simple example of how to use AgentMatrix:

```python
from agentmatrix import DuckDuckGoAgent, LLMAgent

# Initialize agents
ddg_agent = DuckDuckGoAgent()
llm_agent = LLMAgent(api_key="your-openai-api-key", model="gpt-3.5-turbo")

# Use DuckDuckGo agent
search_results = ddg_agent.process("Python programming")

# Use LLM agent
llm_response = llm_agent.process(
    expert_type="Python Expert",
    expert_description="An expert in Python programming",
    user_prompt="Explain list comprehensions",
    response_format="JSON",
    duckduckgo_results=search_results
)

print(llm_response)
```

## Documentation

For detailed documentation, please visit our [GitHub Wiki](https://github.com/kiranbeethoju/agentmatrix/wiki).

## Contributing

We welcome contributions from the community! Here are some ways you can contribute:

1. **Feature Additions**: Have an idea for a new agent type or functionality? We'd love to hear it! Open an issue to discuss your idea or submit a pull request with your implementation.

2. **Bug Fixes**: Found a bug? Please open an issue describing the problem or submit a pull request with a fix.

3. **Documentation**: Help improve our documentation by fixing errors or adding examples.

4. **Testing**: Expand our test coverage or improve existing tests.

To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## Roadmap

- [ ] Add support for more LLM providers
- [ ] Implement agent chaining and workflows
- [ ] Create a web interface for agent management
- [ ] Develop more specialized agents (e.g., for data analysis, code generation)
- [ ] Implement caching mechanisms for improved performance

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Kiran Beethoju - [@kiranbeethoju](https://twitter.com/kiranbeethoju)

Project Link: [https://github.com/kiranbeethoju/agentmatrix](https://github.com/kiranbeethoju/agentmatrix)

## Acknowledgements

- OpenAI for their amazing language models
- DuckDuckGo for their search API
- All the contributors who have helped shape this project

Join us in making LLM agent frameworks more powerful and accessible!
