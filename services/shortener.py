import random
import string

import validators

from database import Database
from models import Url
from repositories import UrlRepository


class ShortenerServiceError(Exception): ...


class ShortenerServiceValidationError(Exception): ...


class ShortenerService:
    def __init__(self):
        db = Database()
        self.repository = UrlRepository(db.get_engine())

    def _is_valid_url(self, url: str) -> bool:
        try:
            return validators.url(url)
        except Exception as e:
            raise ShortenerServiceValidationError("Invalid URL value") from e

    def short(self, url: str) -> Url:
        try:
            if not self._is_valid_url(url):
                raise ShortenerServiceValidationError("Invalid URL value")

            while True:
                url_code = "".join(
                    random.choices(string.ascii_letters + string.digits, k=12)
                )

                if not self.get_url_by_code(url_code):
                    break

            url = Url(url=url, url_code=url_code)

            return self.repository.save(url)
        except Exception as e:
            raise ShortenerServiceError(
                "An error has occurred while short URL"
            ) from e

    def get_url_by_code(self, code: str) -> Url | None:
        try:
            return self.repository.get_by_url_code(code)
        except Exception as e:
            raise ShortenerServiceError(
                "An error has occurred while get url by code"
            ) from e
