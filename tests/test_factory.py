"""Tests for Google ADK agent creation."""

from pathlib import Path

from adk_factory.factory import AgentFactory


def test_create_agent_from_file(tmp_path: Path) -> None:
    (tmp_path / "prompt.md").write_text(
        "You are a test assistant.",
        encoding="utf-8",
    )
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

    agent = AgentFactory().create_from_file(config_file)

    assert agent.name == "test_agent"
    assert agent.model == "gemini-2.5-flash"
    assert agent.instruction == "You are a test assistant."
