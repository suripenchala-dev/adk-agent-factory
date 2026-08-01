"""YAML configuration loading."""

from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from adk_factory.config.models import AgentConfig
from adk_factory.exceptions import ConfigurationError


class ConfigLoader:
    """Load and validate agent configuration files."""

    def load(self, path: str | Path) -> AgentConfig:
        """Load one YAML file and return a validated configuration."""
        config_path = Path(path).expanduser().resolve()

        if not config_path.is_file():
            raise ConfigurationError(
                f"Agent configuration file does not exist: {config_path}"
            )

        try:
            with config_path.open("r", encoding="utf-8") as stream:
                raw_data: Any = yaml.safe_load(stream)
        except (OSError, yaml.YAMLError) as exc:
            raise ConfigurationError(
                f"Unable to read agent configuration: {config_path}"
            ) from exc

        if not isinstance(raw_data, dict):
            raise ConfigurationError(
                f"Agent configuration must be a YAML mapping: {config_path}"
            )

        try:
            return AgentConfig.model_validate(raw_data)
        except ValidationError as exc:
            raise ConfigurationError(
                f"Invalid agent configuration in {config_path}: {exc}"
            ) from exc
