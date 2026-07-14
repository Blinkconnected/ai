from fastapi import APIRouter

from app.services.customer_service import CustomerService

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)

service = CustomerService()


@router.get("/")
def list_customers():

    return service.list()


@router.get("/{customer}")
def get_customer(customer: str):

    return service.get(customer)
