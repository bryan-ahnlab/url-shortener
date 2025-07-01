import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from core.setting import settings

from db.database import Base, createDatabaseEngine, dropDatabaseEngine

from routes.short_url_route import short_url_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # Next.js Server Component 요청으로 인해 무의미
    allow_credentials=True,  # 공식 명세 (WHATWG Fetch: https://fetch.spec.whatwg.org/#http-access-control-allow-origin)
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(short_url_router)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "type": f"{request.base_url}docs",
            "title": "Error",
            "status": exc.status_code,
            "detail": exc.detail or "Unexpected error",
            "instance": str(request.url),
            "method": request.method,
        },
    )


@app.on_event("startup")
async def startup_event():
    if settings.SQLALCHEMY_DATABASE_URL is None:
        raise ValueError("SQLALCHEMY_DATABASE_URL is not set")

    engine = createDatabaseEngine(settings.SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def shutdown_event():
    dropDatabaseEngine()


if __name__ == "__main__":
    if settings.ENVIRONMENT == "development":
        workers = 1
        reload = True
    elif settings.ENVIRONMENT == "production":
        workers = 4
        reload = True
    else:
        workers = 1
        reload = True

    uvicorn.run(
        app="service:app",
        host="0.0.0.0",
        port=settings.PORT,
        access_log=True,
        workers=workers,
        reload=reload,
    )
