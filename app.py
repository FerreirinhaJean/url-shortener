from datetime import UTC, datetime
from http import HTTPStatus

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse

from configs import FastApiConfig
from database import Database
from DTOs import (
    ErrorResponse,
    FieldError,
    UrlRequestDTO,
    UrlResponseDTO,
)
from repositories import UrlRepository
from services import CodeGenerator, ShortenerService, UrlValidator

load_dotenv()
app = FastAPI(**FastApiConfig)


def get_shortener_service() -> ShortenerService:
    return ShortenerService(
        repository=UrlRepository(Database().get_engine()),
        validator=UrlValidator(),
        code_generator=CodeGenerator(),
    )


service = get_shortener_service()


@app.post("/shorten-url", tags=["URLs"])
def url_shortener(item: UrlRequestDTO, req: Request) -> UrlResponseDTO:
    url = service.short(item.url)

    return {"url": item.url, "short_url": str(req.base_url) + url.url_code}


@app.get("/{short_code}", response_class=RedirectResponse, tags=["URLs"])
def redirect(short_code: str):
    url = service.get_url_by_code(short_code)
    if not url:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return RedirectResponse(url=url.url, status_code=HTTPStatus.FOUND)


@app.exception_handler(RequestValidationError)
def validation_error(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    field_errors: list[FieldError] = []
    for error in exc.errors():
        field_errors.append(
            FieldError(field=error["loc"][1], message=error["msg"])
        )

    error_response = ErrorResponse(
        status=HTTPStatus.UNPROCESSABLE_ENTITY.value,
        error=HTTPStatus.UNPROCESSABLE_ENTITY.name,
        message="Validation failed",
        errors=field_errors,
        timestamp=datetime.now(UTC),
    )

    return JSONResponse(
        status_code=error_response["status"],
        content=jsonable_encoder(error_response),
    )


@app.exception_handler(Exception)
def exception(request: Request, exc: Exception) -> JSONResponse:
    error_response = ErrorResponse(
        status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        error=HTTPStatus.INTERNAL_SERVER_ERROR.name,
        message="internal server error",
        errors=[],
        timestamp=datetime.now(UTC),
    )

    return JSONResponse(
        status_code=error_response["status"],
        content=jsonable_encoder(error_response),
    )
