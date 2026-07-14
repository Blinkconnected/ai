from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all Blink AI tools.
    """

    name: str = ""
    description: str = ""

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool."""
        raise NotImplementedError
