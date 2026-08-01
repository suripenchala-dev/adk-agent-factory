"""Tests for YAML configuration loading."""

from pathlib import Path

import pytest

from adk_factory.config.loader import ConfigLoader
from adk_factory.exceptions import ConfigurationError


def test_load_valid_configuration(tmp_path: Path) -> None:
    config_file = tmp_path / "agent.yaml"
    config_file.write_text(
        """
name: test_agent
model: gemini-2.5-flash
description: Test agent
prompt: prompt.md
tools: []
""".strip(),
        encoding="utf-8",
    )

    config = ConfigLoader().load(config_file)

    assert config.name == "test_agent"
    assert config.model == "gemini-2.5-flash"
    assert config.prompt == "prompt.md"


def test_missing_configuration_raises_framework_error() -> None:
    with pytest.raises(ConfigurationError, match="does not exist"):
        ConfigLoader().load("missing.yaml")


def test_unknown_field_is_rejected(tmp_path: Path) -> None:
    config_file = tmp_path / "agent.yaml"
    config_file.write_text(
        """
name: test_agent
prompt: prompt.md
unexpected: true
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ConfigurationError, match="Invalid agent configuration"):
        ConfigLoader().load(config_file)
