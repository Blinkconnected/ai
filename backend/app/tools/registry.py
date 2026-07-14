from app.tools.base import BaseTool


class ToolRegistry:

    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """Register a tool instance by its unique name."""
        if not tool.name:
            raise ValueError("Tool must define a non-empty name.")
        if tool.name in self._tools:
            raise ValueError(f"Tool '{tool.name}' is already registered.")

        self._tools[tool.name] = tool

    def unregister(self, name: str) -> None:
        """Remove a registered tool by name."""
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' is not registered.")

        del self._tools[name]

    def get(self, name: str) -> BaseTool:
        """Return the registered tool instance for the given name."""
        return self._tools[name]

    def list(self) -> list[str]:
        """Return the names of all registered tools."""
        return list(self._tools.keys())
