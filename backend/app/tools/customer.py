from app.connectors.erpnext import ERPNextConnector
from app.tools.base import BaseTool


class CustomerListTool(BaseTool):

    name = "customer.list"

    description = "Return ERPNext customers."

    def __init__(self):
        self.erp = ERPNextConnector()

    def execute(self, **kwargs):

        return self.erp.get(
            "/api/resource/Customer",
            {
                "fields": '["name","customer_name"]',
                "limit_page_length": kwargs.get("limit", 20),
            },
        )
