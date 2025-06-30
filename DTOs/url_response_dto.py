from pydantic import BaseModel


class UrlResponseDTO(BaseModel):
    url: str
    short_url: str
