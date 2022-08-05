from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse
from mms.models.customer import customer
from mms.dependencies import get_db
from mms.schemas.customer import CustomerCreate, CustomerUpdate

router = APIRouter()

@router.get('/')
def list_customers(*, max_results: Optional[int] = 10, db: Session=Depends(get_db)):
    results = customer.get_multi(db=db, limit=max_results)
    response = {"results": results}
    return response

@router.post('/')
def create_new_customer(customer_in: CustomerCreate, db: Session = Depends(get_db)):
    customer_result = customer.create(db=db, obj_in=customer_in)
    return customer_result

@router.get('/{customer_id}')
def get_customer_by_id(customer_id: int, db:Session = Depends(get_db)):
    result = customer.get(db=db, id=customer_id)
    print(customer_id)
    if not result:
        return HTTPException(status_code=404, detail=f"Customer with ID {customer_id} not found")
    return result

@router.put('/{customer_id}')
def update_customer_by_id(customer_id: int, customer_in: CustomerUpdate, db: Session = Depends(get_db)):
    customer_candidate = customer.get(db=db, id=customer_id)
    if not customer_candidate:
        raise HTTPException(status_code=404, detail=f"Customer with ID: {customer_id} not found")
    updated_customer = customer.update(db=db, db_obj=customer_candidate, obj_in=customer_in)
    return updated_customer

@router.delete('/{customer_id}')
def delete_customer_by_id(customer_id: int, db:Session = Depends(get_db)):
    delete_candidate = customer.get(db=db, id=customer_id)
    if delete_candidate:
        result = customer.delete(db=db, id=customer_id)
        return PlainTextResponse(content="Customer with ID {customer_id} deleted successfully", status_code=200)
    else:
        return PlainTextResponse(status_code=404, content=f"Unable to delete non-existing Customer id# {customer_id}")