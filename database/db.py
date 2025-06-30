import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): ...


class DatabaseEnvironmentError(Exception): ...


class Database:
    def __init__(self):
        try:
            url_connect = URL.create(
                database=os.environ["DB_NAME"],
                username=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                port=os.environ["DB_PORT"],
                host=os.environ["DB_HOST"],
                drivername=os.environ["DB_DRIVER"],
            )

            self._engine = create_engine(url=url_connect)
        except Exception as e:
            raise DatabaseEnvironmentError("") from e

    def get_engine(self) -> Engine:
        return self._engine
