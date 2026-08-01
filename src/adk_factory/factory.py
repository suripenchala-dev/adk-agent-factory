"""Google ADK agent creation."""

from pathlib import Path

from google.adk.agents.llm_agent import Agent

from adk_factory.config.loader import ConfigLoader
from adk_factory.config.models import AgentConfig
from adk_factory.prompts.loader import PromptLoader


class AgentFactory:
    """Create Google ADK agents from validated configuration."""

    def __init__(
        self,
        config_loader: ConfigLoader | None = None,
        prompt_loader: PromptLoader | None = None,
    ) -> None:
        self._config_loader = config_loader or ConfigLoader()
        self._prompt_loader = prompt_loader or PromptLoader()

    def create(self, config: AgentConfig, base_directory: str | Path) -> Agent:
        """Create an ADK agent from an in-memory configuration."""
        base_path = Path(base_directory).expanduser().resolve()
        instruction = self._prompt_loader.load(base_path / config.prompt)

        if config.tools:
            raise NotImplementedError(
                "Tool resolution will be added in the next framework milestone."
            )

        return Agent(
            name=config.name,
            model=config.model,
            description=config.description,
            instruction=instruction,
            tools=[],
        )

    def create_from_file(self, config_path: str | Path) -> Agent:
        """Create an ADK agent from a YAML configuration file."""
        resolved_path = Path(config_path).expanduser().resolve()
        config = self._config_loader.load(resolved_path)
        return self.create(config, resolved_path.parent)
