from models import Url
from repositories import UrlRepository
from services.code_generator import CodeGenerator
from services.url_validator import UrlValidator, UrlValidatorError


class ShortenerServiceError(Exception): ...


class ShortenerServiceValidationError(Exception): ...


class ShortenerService:
    def __init__(
        self,
        repository: UrlRepository,
        validator: UrlValidator,
        code_generator: CodeGenerator,
    ):
        self.repository = repository
        self.validator = validator
        self.code_generator = code_generator

    def short(self, url: str) -> Url:
        try:
            self.validator.validate(url)

            while True:
                url_code = self.code_generator.generate()

                if not self.get_url_by_code(url_code):
                    break

            url = Url(url=url, url_code=url_code)

            return self.repository.save(url)
        except UrlValidatorError as e:
            raise ShortenerServiceError("Invalid URL value") from e
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
