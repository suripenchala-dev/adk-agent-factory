"""Pydantic models for agent configuration."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AgentConfig(BaseModel):
    """Validated configuration required to generate an ADK agent."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(min_length=1, pattern=r"^[A-Za-z_][A-Za-z0-9_]*$")
    model: str = Field(default="gemini-2.5-flash", min_length=1)
    description: str = Field(default="", max_length=1_000)
    prompt: str = Field(min_length=1)
    tools: list[str] = Field(default_factory=list)

    @field_validator("name", "model", "prompt", "description")
    @classmethod
    def strip_text(cls, value: str) -> str:
        """Remove accidental leading and trailing whitespace."""
        return value.strip()

    @field_validator("tools")
    @classmethod
    def validate_tools(cls, tools: list[str]) -> list[str]:
        """Normalize tool names and reject empty or duplicate entries."""
        normalized = [tool.strip() for tool in tools]

        if any(not tool for tool in normalized):
            raise ValueError("Tool names cannot be empty.")

        if len(normalized) != len(set(normalized)):
            raise ValueError("Tool names must be unique.")

        return normalized
