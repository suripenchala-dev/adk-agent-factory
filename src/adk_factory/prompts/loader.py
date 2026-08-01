"""Markdown prompt loading."""

from pathlib import Path

from adk_factory.exceptions import PromptLoadError


class PromptLoader:
    """Load agent instructions from Markdown files."""

    def load(self, path: str | Path) -> str:
        """Read a UTF-8 Markdown prompt and return its content."""
        prompt_path = Path(path).expanduser().resolve()

        if not prompt_path.is_file():
            raise PromptLoadError(f"Prompt file does not exist: {prompt_path}")

        try:
            content = prompt_path.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise PromptLoadError(f"Unable to read prompt file: {prompt_path}") from exc

        if not content:
            raise PromptLoadError(f"Prompt file is empty: {prompt_path}")

        return content
