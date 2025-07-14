import validators


class UrlValidatorError(Exception): ...


class UrlValidator:
    def validate(self, url: str) -> None:
        try:
            validators.url(url)
        except Exception as e:
            raise UrlValidatorError("Invalid URL value") from e
