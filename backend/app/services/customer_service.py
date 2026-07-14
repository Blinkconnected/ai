from app.connectors.erpnext import ERPNextConnector


class CustomerService:
    """Customer business logic."""

    def __init__(self):
        self.erp = ERPNextConnector()

    def list(self, limit: int = 20):

        return self.erp.get(
            "/api/resource/Customer",
            params={
                "fields": '["name","customer_name"]',
                "limit_page_length": limit,
            },
        )

    def get(self, customer_name: str):

        return self.erp.get(f"/api/resource/Customer/{customer_name}")
