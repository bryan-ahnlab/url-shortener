from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from schemas import service
from crud import crud

service_router = APIRouter()

@service_router.post("/url", response_class=JSONResponse)
async def create_url(request: service.CreateURL):

    item = crud.create_url(request)

    response = {
        "status_code": status.HTTP_200_OK,
        "message": "created",
        "data": {
            "request": request,
            "item": item,    
        }        
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response))

@service_router.get("/{short_url}")
async def read_url(short_url: str):
    request = service.ReadURL(short_url=short_url)

    item = crud.read_url(request)
    if item is None:
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "not found",
            "data": {
                "request": request,
                "item": item,    
            }        
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response))

    long_url = item.long_url    
    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        long_url = "http://" + long_url

    return RedirectResponse(url=long_url, status_code=302)