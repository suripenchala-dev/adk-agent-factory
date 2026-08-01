"""Framework-specific exceptions."""


class AdkFactoryError(Exception):
    """Base exception for all ADK Agent Factory errors."""


class ConfigurationError(AdkFactoryError):
    """Raised when an agent configuration cannot be loaded or validated."""


class PromptLoadError(AdkFactoryError):
    """Raised when an agent prompt cannot be loaded."""
