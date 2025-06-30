from pydantic import BaseModel


class UrlResponse(BaseModel):
    url: str
    short_url: str
