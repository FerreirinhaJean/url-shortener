from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from models import Url


class UrlRepositoryError(Exception): ...


class UrlRepository:
    def __init__(self, engine: Engine):
        self._session_factory = sessionmaker(bind=engine)

    def save(self, item: Url) -> Url:
        try:
            with self._session_factory() as session:
                session.add(item)
                session.commit()
                session.refresh(item)

                return item
        except Exception as e:
            raise UrlRepositoryError("Save url error in UrlRepository") from e

    def get_by_url_code(self, code: str) -> Url | None:
        try:
            stmt = select(Url).where(Url.url_code == code)
            with self._session_factory() as session:
                result = session.execute(stmt).first()

            return result[0] if result else None
        except Exception as e:
            raise UrlRepositoryError(
                "Get by url_shortener error from UrlRepository"
            ) from e
