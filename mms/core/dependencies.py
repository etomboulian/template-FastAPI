from typing import Generator

from mms.db import Session


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()