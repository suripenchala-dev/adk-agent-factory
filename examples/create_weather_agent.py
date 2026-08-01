"""Create the example weather agent."""

from adk_factory import AgentFactory


def main() -> None:
    """Build the example agent and print basic information."""
    agent = AgentFactory().create_from_file(
        "examples/weather_agent/agent.yaml"
    )
    print(f"Created agent: {agent.name}")
    print(f"Model: {agent.model}")


if __name__ == "__main__":
    main()
