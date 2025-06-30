from pydantic import BaseModel


class UrlRequestDTO(BaseModel):
    url: str
