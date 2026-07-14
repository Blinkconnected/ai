from abc import ABC, abstractmethod
from typing import Any

ToolResult = Any


class BaseTool(ABC):
    """Base interface for Blink AI tools.

    Concrete tools must expose a stable `name`, a human-readable
    `description`, and an `execute` method accepting keyword arguments.
    """

    name: str = ""
    description: str = ""

    @abstractmethod
    def execute(self, **kwargs: Any) -> ToolResult:
        """Execute the tool with keyword arguments."""
        ...
