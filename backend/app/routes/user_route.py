from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import user_schema
from schemas import user_activity_history_schema

from crud import user_crud
from crud import user_activity_history_crud


user_router = APIRouter()


@user_router.post(
    "/user", response_class=JSONResponse, response_model=user_schema.CreateUserResponse
)
async def create_user(request: Request, payload: user_schema.CreateUserRequest):
    try:
        existing_user = user_crud.read_user_by_email(payload.email)
        if existing_user:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={
                    "type": f"{base_url}/docs#/default/create_user_user_post",
                    "title": "Conflict",
                    "status": status.HTTP_409_CONFLICT,
                    "detail": "User already exists.",
                    "instance": instance,
                    "method": "POST",
                },
            )

        user = user_crud.create_user(payload)

        client_ip = request.headers.get("X-Forwarded-For") or (
            request.client.host if request.client else None
        )
        user_agent = request.headers.get("User-Agent")
        location = request.headers.get("X-Geo-Location")

        user_activity_history_crud.create_user_activity_history(
            request=user_activity_history_schema.CreateUserActivityHistoryRequest(
                user_id=user.id,
                activity_type="CREATE",
                description="User created",
                ip_address=client_ip,
                user_agent=user_agent,
                location=location,
            ),
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "create",
                    "request": payload,
                    "response": user,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/create_user_user_post",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "POST",
            },
        )


@user_router.get(
    "/user/{id}",
    response_class=JSONResponse,
    response_model=user_schema.ReadUserResponse,
)
async def read_user(request: Request, payload: user_schema.ReadUserRequest = Depends()):
    try:
        existing_user = user_crud.read_user(payload)
        if not existing_user:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "type": f"{base_url}/docs#/default/read_user_user__id__get",
                    "title": "Not Found",
                    "status": status.HTTP_404_NOT_FOUND,
                    "detail": "User not found.",
                    "instance": instance,
                    "method": "GET",
                },
            )

        client_ip = request.headers.get("X-Forwarded-For") or (
            request.client.host if request.client else None
        )
        user_agent = request.headers.get("User-Agent")
        location = request.headers.get("X-Geo-Location")

        user_activity_history_crud.create_user_activity_history(
            request=user_activity_history_schema.CreateUserActivityHistoryRequest(
                user_id=existing_user.id,
                activity_type="READ",
                description="User read",
                ip_address=client_ip,
                user_agent=user_agent,
                location=location,
            ),
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "read",
                    "request": payload,
                    "response": existing_user,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/read_user_user__id__get",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "GET",
            },
        )


@user_router.put(
    "/user", response_class=JSONResponse, response_model=user_schema.UpdateUserResponse
)
async def update_user(request: Request, payload: user_schema.UpdateUserRequest):
    try:
        existing_user = user_crud.read_user(payload)
        if not existing_user:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "type": f"{base_url}/docs#/default/update_user_user_put",
                    "title": "Not Found",
                    "status": status.HTTP_404_NOT_FOUND,
                    "detail": "User not found.",
                    "instance": instance,
                    "method": "PUT",
                },
            )

        user = user_crud.update_user(payload)

        client_ip = request.headers.get("X-Forwarded-For") or (
            request.client.host if request.client else None
        )
        user_agent = request.headers.get("User-Agent")
        location = request.headers.get("X-Geo-Location")

        user_activity_history_crud.create_user_activity_history(
            request=user_activity_history_schema.CreateUserActivityHistoryRequest(
                user_id=existing_user.id,
                activity_type="UPDATE",
                description="User updated",
                ip_address=client_ip,
                user_agent=user_agent,
                location=location,
            ),
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "update",
                    "request": payload,
                    "response": user,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/update_user_user_put",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "PUT",
            },
        )


@user_router.delete(
    "/user", response_class=JSONResponse, response_model=user_schema.DeleteUserResponse
)
async def delete_user(
    request: Request,
    payload: user_schema.DeleteUserRequest = Depends(),
):
    try:
        existing_user = user_crud.read_user(payload)
        if not existing_user:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "type": f"{base_url}/docs#/default/delete_user_user_delete",
                    "title": "Not Found",
                    "status": status.HTTP_404_NOT_FOUND,
                    "detail": "User not found.",
                    "instance": instance,
                    "method": "DELETE",
                },
            )

        if existing_user.email != payload.email:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "type": f"{base_url}/docs#/default/delete_user_user_delete",
                    "title": "Bad Request",
                    "status": status.HTTP_400_BAD_REQUEST,
                    "detail": "Email does not match.",
                    "instance": instance,
                    "method": "DELETE",
                },
            )

        if not user_crud.verify_password(payload.password, existing_user.password):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "type": f"{base_url}/docs#/default/delete_user_user_delete",
                    "title": "Unauthorized",
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "detail": "Invalid password.",
                    "instance": instance,
                    "method": "DELETE",
                },
            )

        user = user_crud.delete_user(payload)

        client_ip = request.headers.get("X-Forwarded-For") or (
            request.client.host if request.client else None
        )
        user_agent = request.headers.get("User-Agent")
        location = request.headers.get("X-Geo-Location")

        user_activity_history_crud.create_user_activity_history(
            request=user_activity_history_schema.CreateUserActivityHistoryRequest(
                user_id=existing_user.id,
                activity_type="DELETE",
                description="User deleted",
                ip_address=client_ip,
                user_agent=user_agent,
                location=location,
            ),
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "delete",
                    "request": payload,
                    "response": user,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/delete_user_user_delete",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "DELETE",
            },
        )


@user_router.post(
    "/user/login",
    response_class=JSONResponse,
    response_model=user_schema.LoginUserResponse,
)
async def login_user(request: Request, payload: user_schema.LoginUserRequest):
    try:
        existing_user = user_crud.read_user_by_email(payload.email)
        if not existing_user:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "type": f"{base_url}/docs#/default/login_user_user_login_post",
                    "title": "Not Found",
                    "status": status.HTTP_404_NOT_FOUND,
                    "detail": "User not found.",
                    "instance": instance,
                    "method": "POST",
                },
            )

        if not user_crud.verify_password(payload.password, existing_user.password):
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "type": f"{base_url}/docs#/default/login_user_user_login_post",
                    "title": "Unauthorized",
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "detail": "Invalid email or password.",
                    "instance": instance,
                    "method": "POST",
                },
            )

        client_ip = request.headers.get("X-Forwarded-For") or (
            request.client.host if request.client else None
        )
        user_agent = request.headers.get("User-Agent")
        location = request.headers.get("X-Geo-Location")

        user_activity_history_crud.create_user_activity_history(
            request=user_activity_history_schema.CreateUserActivityHistoryRequest(
                user_id=existing_user.id,
                activity_type="LOGIN",
                description="User logged in",
                ip_address=client_ip,
                user_agent=user_agent,
                location=location,
            ),
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "read",
                    "request": payload,
                    "response": existing_user,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/login_user_user_login_post",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "POST",
            },
        )
