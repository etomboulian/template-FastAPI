from pydantic import BaseModel

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class CustomerDB(CustomerBase):
    id: int

class Customer(CustomerDB):
    pass

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    id: int

    class Config:
        orm_mode = True
