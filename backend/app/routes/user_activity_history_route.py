from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import user_activity_history_schema
from crud import user_crud
from crud import user_activity_history_crud


user_activity_history_router = APIRouter()


@user_activity_history_router.post(
    "/user-activity-history",
    response_class=JSONResponse,
    response_model=user_activity_history_schema.CreateUserActivityHistoryResponse,
)
async def create_user_activity_history(
    request: Request,
    payload: user_activity_history_schema.CreateUserActivityHistoryRequest,
):
    try:
        history = user_activity_history_crud.create_user_activity_history(payload)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "create",
                    "request": payload,
                    "response": history,
                }
            ),
        )
    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/create_user_activity_history_user_activity_history_post",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "POST",
            },
        )


@user_activity_history_router.get(
    "/user-activity-history/{id}",
    response_class=JSONResponse,
    response_model=user_activity_history_schema.ReadUserActivityHistoryResponse,
)
async def read_user_activity_history(
    request: Request,
    payload: user_activity_history_schema.ReadUserActivityHistoryRequest = Depends(),
):
    try:
        existing_history = user_activity_history_crud.read_user_activity_history(
            payload
        )

        if not existing_history:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return (
                JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "type": f"{base_url}/docs#/default/read_user_activity_history_user_activity_history__id__get",
                        "title": "Not Found",
                        "status": status.HTTP_404_NOT_FOUND,
                        "detail": "User activity history not found.",
                    },
                ),
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "read",
                    "request": payload,
                    "response": existing_history,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/read_user_activity_history_user_activity_history__id__get",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "GET",
            },
        )


@user_activity_history_router.put(
    "/user-activity-history",
    response_class=JSONResponse,
    response_model=user_activity_history_schema.UpdateUserActivityHistoryResponse,
)
async def update_user_activity_history(
    request: Request,
    payload: user_activity_history_schema.UpdateUserActivityHistoryRequest = Depends(),
):
    try:
        existing_history = user_activity_history_crud.read_user_activity_history(
            payload
        )
        if not existing_history:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return (
                JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "type": f"{base_url}/docs#/default/update_user_activity_history_user_activity_history_put",
                        "title": "Not Found",
                        "status": status.HTTP_404_NOT_FOUND,
                        "detail": "User activity history not found.",
                        "instance": instance,
                        "method": "PUT",
                    },
                ),
            )

        history = user_activity_history_crud.update_user_activity_history(payload)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "update",
                    "request": payload,
                    "response": history,
                }
            ),
        )
    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/update_user_activity_history_user_activity_history_put",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "PUT",
            },
        )


@user_activity_history_router.delete(
    "/user-activity-history",
    response_class=JSONResponse,
    response_model=user_activity_history_schema.DeleteUserActivityHistoryResponse,
)
async def delete_user_activity_history(
    request: Request,
    payload: user_activity_history_schema.DeleteUserActivityHistoryRequest,
):
    try:
        existing_history = user_activity_history_crud.read_user_activity_history(
            payload
        )
        if not existing_history:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return (
                JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "type": f"{base_url}/docs#/default/delete_user_activity_history_user_activity_history_delete",
                        "title": "Not Found",
                        "status": status.HTTP_404_NOT_FOUND,
                        "detail": "User activity history not found.",
                        "instance": instance,
                        "method": "DELETE",
                    },
                ),
            )

        history = user_activity_history_crud.delete_user_activity_history(payload)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "delete",
                    "request": payload,
                    "response": history,
                }
            ),
        )
    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/delete_user_activity_history_user_activity_history_delete",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "DELETE",
            },
        )


@user_activity_history_router.get(
    "/user-activity-history/user/{user_id}",
    response_class=JSONResponse,
    response_model=user_activity_history_schema.ReadUserActivityHistoryByUserIdResponse,
)
async def read_user_activity_history_by_user_id(
    request: Request,
    payload: user_activity_history_schema.ReadUserActivityHistoryByUserIdRequest = Depends(),
):
    try:
        existing_histories = (
            user_activity_history_crud.read_user_activity_history_by_user_id(payload)
        )

        if not existing_histories:
            base_url = str(request.base_url).rstrip("/")
            instance = str(request.url)

            return (
                JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "type": f"{base_url}/docs#/default/read_user_activity_history_user_activity_history_user__user_id__get",
                        "title": "Not Found",
                        "status": status.HTTP_404_NOT_FOUND,
                        "detail": "User activity history not found.",
                        "instance": instance,
                        "method": "GET",
                    },
                ),
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "status": status.HTTP_200_OK,
                    "message": "read",
                    "request": payload,
                    "response": existing_histories,
                }
            ),
        )

    except Exception as error:
        base_url = str(request.base_url).rstrip("/")
        instance = str(request.url)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "type": f"{base_url}/docs#/default/read_user_activity_history_user_activity_history_user__user_id__get",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": str(error),
                "instance": instance,
                "method": "GET",
            },
        )
