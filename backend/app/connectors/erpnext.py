from app.connectors.base import BaseConnector
from app.core.config import get_settings


class ERPNextConnector(BaseConnector):

    def __init__(self):
        settings = get_settings()

        super().__init__(
            base_url=settings.ERP_URL,
            headers={
                "Authorization": (
                    f"token {settings.ERP_API_KEY}:{settings.ERP_API_SECRET}"
                ),
                "Content-Type": "application/json",
            },
        )
