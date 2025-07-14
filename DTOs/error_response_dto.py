from datetime import datetime
from typing import Any, TypedDict


class FieldError(TypedDict):
    field: str
    message: str


class ErrorResponse(TypedDict):
    status: int
    error: str
    message: str
    errors: list[FieldError] | list[Any]
    timestamp: datetime
