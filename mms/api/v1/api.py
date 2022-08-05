from fastapi import APIRouter
from mms.api.v1.endpoints import customer

api_router = APIRouter()
api_router.include_router(customer.router, prefix='/customers', tags=["customers"])