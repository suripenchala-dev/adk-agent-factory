"""Tests for Markdown prompt loading."""

from pathlib import Path

import pytest

from adk_factory.exceptions import PromptLoadError
from adk_factory.prompts.loader import PromptLoader


def test_load_prompt(tmp_path: Path) -> None:
    prompt_file = tmp_path / "prompt.md"
    prompt_file.write_text("# Role\n\nYou are helpful.", encoding="utf-8")

    assert PromptLoader().load(prompt_file) == "# Role\n\nYou are helpful."


def test_empty_prompt_is_rejected(tmp_path: Path) -> None:
    prompt_file = tmp_path / "prompt.md"
    prompt_file.write_text("   ", encoding="utf-8")

    with pytest.raises(PromptLoadError, match="empty"):
        PromptLoader().load(prompt_file)
