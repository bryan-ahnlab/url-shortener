import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from contextlib import asynccontextmanager

from core.setting import settings
from db.database import Base, createDatabaseEngine, dropDatabaseEngine

from routes.user_route import user_router
from routes.user_activity_history_route import user_activity_history_router
from routes.short_url_route import short_url_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.SQLALCHEMY_DATABASE_URL is None:
        raise ValueError("SQLALCHEMY_DATABASE_URL is not set")

    engine = createDatabaseEngine(settings.SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("✅ Database connected")

    yield  # 앱이 실행되는 동안 여기서 대기

    dropDatabaseEngine()
    print("🛑 Database disconnected")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # Next.js Server Component 요청으로 인해 무의미하지만, 명시
    allow_credentials=True,  # 공식 명세 (WHATWG Fetch: https://fetch.spec.whatwg.org/#http-access-control-allow-origin)
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(user_router)
app.include_router(user_activity_history_router)
app.include_router(short_url_router)


# 커스텀 예외 처리
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


if __name__ == "__main__":
    if settings.ENVIRONMENT == "development":
        workers = 1
        reload = True
    elif settings.ENVIRONMENT == "production":
        workers = 4
        reload = False
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
