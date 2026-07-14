from unittest.mock import MagicMock

import pytest

from app.tools.base import BaseTool
from app.tools.customer import CustomerListTool
from app.tools.registry import ToolRegistry


class DummyTool(BaseTool):
    name = "dummy.tool"
    description = "A dummy tool for testing"

    def execute(self, **kwargs):
        return {"ok": True, "kwargs": kwargs}


def test_tool_registry_register_get_list():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)

    assert registry.list() == ["dummy.tool"]
    assert registry.get("dummy.tool") is tool
    assert registry.get("dummy.tool").execute(test=123) == {
        "ok": True,
        "kwargs": {"test": 123},
    }


def test_tool_registry_duplicate_registration_raises_value_error():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)

    with pytest.raises(ValueError, match="already registered"):
        registry.register(tool)


def test_tool_registry_unregister_removes_tool():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)
    registry.unregister("dummy.tool")

    assert registry.list() == []
    with pytest.raises(KeyError):
        registry.get("dummy.tool")


def test_tool_registry_unregister_missing_tool_raises_key_error():
    registry = ToolRegistry()

    with pytest.raises(KeyError, match="not registered"):
        registry.unregister("missing.tool")


def test_tool_exposes_metadata():
    tool = DummyTool()

    assert tool.name == "dummy.tool"
    assert tool.description == "A dummy tool for testing"


def test_customer_list_tool_uses_customer_service_default_limit():
    service = MagicMock()
    service.list.return_value = [{"name": "CUST-001"}]

    tool = CustomerListTool(service=service)
    result = tool.execute()

    service.list.assert_called_once_with(limit=20)
    assert result == [{"name": "CUST-001"}]


def test_customer_list_tool_uses_customer_service_custom_limit():
    service = MagicMock()
    service.list.return_value = [{"name": "CUST-002"}]

    tool = CustomerListTool(service=service)
    result = tool.execute(limit=5)

    service.list.assert_called_once_with(limit=5)
    assert result == [{"name": "CUST-002"}]
