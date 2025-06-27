from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import user_schema
from crud import user_crud

user_router = APIRouter()


@user_router.post(
    "/signup", response_class=JSONResponse, response_model=user_schema.SignUpResponse
)
async def signup(request: Request, payload: user_schema.SignUpRequest):
    try:
        if user_crud.get_user_by_email(payload.email):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/signup_signup_post",
                "title": "Conflict",
                "status": status.HTTP_409_CONFLICT,
                "detail": "User already exists.",
                "instance": instance,
            }
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT, content=error_response
            )

        user = user_crud.create_user(payload)

        response = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "phone": user.phone,
            "address": user.address,
            "birth": user.birth,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/signup_signup_post",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )


@user_router.post(
    "/login", response_class=JSONResponse, response_model=user_schema.LoginResponse
)
async def login(request: Request, payload: user_schema.LoginRequest):
    try:
        user = user_crud.get_user_by_email(payload.email)

        if not user or not user_crud.verify_password(payload.password, user.password):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/login_login_post",
                "title": "Unauthorized",
                "status": status.HTTP_401_UNAUTHORIZED,
                "detail": "Invalid email or password.",
                "instance": instance,
            }
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED, content=error_response
            )

        response = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/login_login_post",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )


@user_router.put(
    "/update/{email}",
    response_class=JSONResponse,
    response_model=user_schema.SignUpResponse,
)
async def update(request: Request, email: str, payload: user_schema.UpdateRequest):
    try:
        user = user_crud.update_user(email, payload)

        if not user:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/update_update_put",
                "title": "Not Found",
                "status": status.HTTP_404_NOT_FOUND,
                "detail": "User not found.",
                "instance": instance,
            }
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content=error_response
            )

        response = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "phone": user.phone,
            "address": user.address,
            "birth": user.birth,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/update_update_put",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )
