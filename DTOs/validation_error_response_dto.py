from datetime import datetime
from typing import TypedDict


class FieldError(TypedDict):
    field: str
    message: str


class ValidationErrorResponse(TypedDict):
    status: int
    error: str
    message: str
    errors: list[FieldError]
    timestamp: datetime
