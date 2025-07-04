from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import user_schema
from crud import user_crud

user_router = APIRouter()


@user_router.post(
    "/user",
    response_class=JSONResponse,
    response_model=user_schema.CreateUserResponse,
)
async def create_user(request: Request, payload: user_schema.CreateUserRequest):
    try:
        if user_crud.read_user_by_email(payload.email):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/create_user_user_post",
                "title": "Conflict",
                "status": status.HTTP_409_CONFLICT,
                "detail": "User already exists.",
                "instance": instance,
                "method": "POST",
            }
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT, content=error_response
            )

        data = user_crud.create_user(payload)

        response = {
            "status": status.HTTP_200_OK,
            "message": "create",
            "request": payload,
            "response": data,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/create_user_user_post",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "POST",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )


@user_router.get("/user/{id}")
async def read_user(request: Request, payload: user_schema.ReadUserRequest = Depends()):
    try:
        data = user_crud.read_user(payload)

        if data is not None:
            response = {
                "status": status.HTTP_200_OK,
                "message": "read",
                "request": payload,
                "response": data,
            }

            return JSONResponse(
                status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
            )

        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/read_user_user__id__get",
            "title": "Resource Not Found",
            "status": status.HTTP_404_NOT_FOUND,
            "detail": f"User '{payload.id}' does not exist.",
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
            "type": f"{base_url}/docs#/default/read_user_user__id__get",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "GET",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )


@user_router.put(
    "/user",
    response_class=JSONResponse,
    response_model=user_schema.UpdateUserResponse,
)
async def update_user(request: Request, payload: user_schema.UpdateUserRequest):
    try:
        if not user_crud.read_user(payload):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/update_user_user_put",
                "title": "Not Found",
                "status": status.HTTP_404_NOT_FOUND,
                "detail": "User not found.",
                "instance": instance,
                "method": "PUT",
            }
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content=error_response
            )

        data = user_crud.update_user(payload)

        response = {
            "status": status.HTTP_200_OK,
            "message": "update",
            "request": payload,
            "response": data,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/update_user_user_put",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "PUT",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )


@user_router.delete("/user", response_class=JSONResponse)
async def delete_user(request: Request, payload: user_schema.DeleteUserRequest):
    try:
        data = user_crud.delete_user(payload.id)

        if not data:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/delete_user_user_delete",
                "title": "Not Found",
                "status": status.HTTP_404_NOT_FOUND,
                "detail": "User not found.",
                "instance": instance,
                "method": "DELETE",
            }
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, content=error_response
            )

        response = {
            "status": status.HTTP_200_OK,
            "message": "delete",
            "request": payload,
            "response": data,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/delete_user_user_delete",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "DELETE",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )


@user_router.post(
    "/user/login",
    response_class=JSONResponse,
    response_model=user_schema.ReadUserResponse,
)
async def login_user(request: Request, payload: user_schema.LoginUserRequest):
    try:
        data = user_crud.read_user_by_email(payload.email)

        if not data or not user_crud.verify_password(payload.password, data.password):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            error_response = {
                "type": f"{base_url}/docs#/default/login_user_user_login_post",
                "title": "Unauthorized",
                "status": status.HTTP_401_UNAUTHORIZED,
                "detail": "Invalid email or password.",
                "instance": instance,
                "method": "POST",
            }
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED, content=error_response
            )

        response = {
            "status": status.HTTP_200_OK,
            "message": "read",
            "request": payload,
            "response": data,
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(response)
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        error_response = {
            "type": f"{base_url}/docs#/default/login_user_user_login_post",
            "title": "Internal Server Error",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
            "instance": instance,
            "method": "POST",
        }
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response
        )
