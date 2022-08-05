from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mms.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)