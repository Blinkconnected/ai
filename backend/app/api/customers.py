from fastapi import APIRouter

from app.connectors.erpnext import ERPNextConnector

router = APIRouter(prefix="/customers", tags=["Customers"])

erp = ERPNextConnector()


@router.get("/")
def list_customers():

    return erp.get(
        "/api/resource/Customer",
        params={
            "fields": '["name","customer_name"]',
            "limit_page_length": 20,
        },
    )
