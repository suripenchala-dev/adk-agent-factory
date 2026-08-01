"""Command-line interface for ADK Agent Factory."""

import argparse
from collections.abc import Sequence

from adk_factory.config.loader import ConfigLoader
from adk_factory.exceptions import AdkFactoryError


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(prog="adk-factory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate an agent YAML configuration.",
    )
    validate_parser.add_argument("config", help="Path to the agent YAML file.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the ADK Agent Factory command-line interface."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "validate":
            config = ConfigLoader().load(args.config)
            print(f"Valid configuration: {config.name}")
            return 0
    except AdkFactoryError as exc:
        parser.exit(status=1, message=f"error: {exc}\n")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
