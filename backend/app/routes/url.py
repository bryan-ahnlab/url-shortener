from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from schemas import url
from crud import crud

url_router = APIRouter()


@url_router.post(
    "/url", response_class=JSONResponse, response_model=url.ShortenUrlResponse
)
async def create_url(request: Request, payload: url.ShortenUrlRequest):
    try:
        data = crud.create_url(payload)

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/create_url_url_post",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )

    response = {
        "status": status.HTTP_200_OK,
        "message": "create",
        "request": payload,
        "data": data,
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
    )


@url_router.get("/{short_url}")
async def read_url(request: Request, payload: url.RedirectUrl = Depends()):
    try:
        data = crud.read_url(payload)

        if data is not None:
            long_url = data.long_url

            if not (long_url.startswith("http://") or long_url.startswith("https://")):
                long_url = "http://" + long_url

            return RedirectResponse(url=long_url, status_code=302)

        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/read_url__short_url__get",
            "title": "Resource Not Found",
            "status": status.HTTP_404_NOT_FOUND,
            "detail": f"Short URL '{payload.short_url}' does not exist.",
            "instance": instance,
        }
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content=error_response
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/read_url__short_url__get",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )
