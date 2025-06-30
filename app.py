from http import HTTPStatus

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse

from configs import FastApiConfig
from DTOs import UrlRequestDTO, UrlResponseDTO
from services import ShortenerService

load_dotenv()
app = FastAPI(**FastApiConfig)
service = ShortenerService()


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
