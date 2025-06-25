from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from schemas import service
from crud import crud

service_router = APIRouter()


@service_router.post("/url", response_class=JSONResponse)
async def create_url(request: service.ShortenURLRequest):

    data = crud.create_url(request)

    response = {
        "status": status.HTTP_200_OK,
        "message": "create",
        "request": request,
        "data": data,
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
    )


@service_router.get("/{short_url}")
async def read_url(short_url: str):
    request = service.RedirectURL(short_url=short_url)

    data = crud.read_url(request)

    if data is not None:
        long_url = data.long_url

        return RedirectResponse(url=long_url, status_code=302)

    response = {
        "status": status.HTTP_404_NOT_FOUND,
        "message": "not found",
        "request": request,
        "data": data,
    }

    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
    )
