"""Tests for the command-line interface."""

from pathlib import Path

from adk_factory.cli import main


def test_validate_command(tmp_path: Path, capsys: object) -> None:
    config_file = tmp_path / "agent.yaml"
    config_file.write_text(
        """
name: test_agent
prompt: prompt.md
tools: []
""".strip(),
        encoding="utf-8",
    )

    result = main(["validate", str(config_file)])

    assert result == 0
