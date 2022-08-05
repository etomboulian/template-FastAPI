from sqlalchemy import Column, Integer, String
from mms.db import Base
from mms.db import CRUDBase
from mms.schemas import Customer, CustomerCreate, CustomerUpdate

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    ...

customer = CRUDCustomer(Customer)