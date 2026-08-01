# ADK Agent Factory

A configuration-driven Python framework for generating Google ADK agents from YAML
configuration and Markdown prompts.

## Current milestone

The current foundation provides:

- A validated `AgentConfig` model
- A safe YAML configuration loader
- A Markdown prompt loader
- A minimal Google ADK agent factory
- A command-line validation command
- Unit tests, linting, type checking, and coverage
- GitHub Actions continuous integration

## Project structure

```text
adk-agent-factory/
├── .github/workflows/ci.yml
├── examples/weather_agent/
│   ├── agent.yaml
│   └── prompt.md
├── src/adk_factory/
│   ├── config/
│   ├── prompts/
│   ├── exceptions.py
│   ├── factory.py
│   └── cli.py
├── tests/
├── pyproject.toml
├── LICENSE
└── README.md
```

## Setup

```bash
uv sync --dev
```

## Validate an agent configuration

```bash
uv run adk-factory validate examples/weather_agent/agent.yaml
```

## Create an ADK agent in Python

```python
from adk_factory import AgentFactory

agent = AgentFactory().create_from_file(
    "examples/weather_agent/agent.yaml"
)

print(agent.name)
```

## Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
```

## Security note

Do not commit API keys. Put local credentials in `.env`, which is excluded by
`.gitignore`.
