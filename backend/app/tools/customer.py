from typing import Any

from app.services.customer_service import CustomerService
from app.tools.base import BaseTool, ToolResult


class CustomerListTool(BaseTool):
    """Tool for listing customers through the customer service."""

    name = "customer.list"
    description = "List ERPNext customers"

    def __init__(self, service: CustomerService | None = None) -> None:
        self.service = service or CustomerService()

    def execute(self, **kwargs: Any) -> ToolResult:
        return self.service.list(limit=kwargs.get("limit", 20))
