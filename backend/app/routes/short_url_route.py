from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from schemas import short_url_schema
from crud import short_url_crud

short_url_router = APIRouter()


@short_url_router.post(
    "/short-url",
    response_class=JSONResponse,
    response_model=short_url_schema.CreateShortUrlResponse,
)
async def create_short_url(
    request: Request, payload: short_url_schema.CreateShortUrlRequest
):
    try:
        # 테스트용 강제 에러
        # raise Exception("Test error")

        data = short_url_crud.create_short_url(payload)

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/create_short_url_short_url_post",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "POST",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )

    response = {
        "status": status.HTTP_200_OK,
        "message": "create",
        "request": payload,
        "response": data,
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
    )


@short_url_router.get("/{short_url}")
async def read_short_url(
    request: Request, payload: short_url_schema.ReadShortUrlRequest = Depends()
):
    try:
        data = short_url_crud.read_short_url(payload)

        if data is not None:
            long_url = data.long_url

            if not (long_url.startswith("http://") or long_url.startswith("https://")):
                long_url = "http://" + long_url

            return RedirectResponse(url=long_url, status_code=302)

        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/read_short_url__short_url_schema__get",
            "title": "Resource Not Found",
            "status": status.HTTP_404_NOT_FOUND,
            "detail": f"Short URL '{payload.short_url}' does not exist.",
            "instance": instance,
            "method": "GET",
        }
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content=error_response
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/read_short_url__short_url_schema__get",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "GET",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )
