from sqlalchemy.orm import Session
from .base import Base
from .session import engine


def init_db(db: Session)-> None:
    Base.metadata.create_all(bind=engine)