import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.setting import settings

from db.database import Base, createDatabaseEngine, dropDatabaseEngine

from routes.service import service_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Next.js Server Component 요청으로 인해 무의미
    allow_credentials=True, # 공식 명세 (WHATWG Fetch: https://fetch.spec.whatwg.org/#http-access-control-allow-origin)
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(service_router)

@app.on_event("startup")
async def startup_event():
    
    engine = createDatabaseEngine(settings.SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown_event():
    dropDatabaseEngine()

if __name__ == "__main__":	
    if settings.ENVIRONMENT == 'development':        
        workers = 1
        reload = True
    elif settings.ENVIRONMENT == 'production':
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
        reload=reload
    )
