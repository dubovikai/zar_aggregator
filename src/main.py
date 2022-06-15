# coding: utf-8
from click import echo
import uvicorn
import logging
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from core.settings import Settings


logger = logging.getLogger('App')

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

settings = Settings()

app = FastAPI(
    title=settings.project_title,
    openapi_url="/schema2.json",
    version='3.0.2',
    docs_url="/docs2",
    redoc_url="/redoc2"
)

engine = create_engine(settings.db_string, echo=settings.is_debug)
Session = sessionmaker(engine)
session = Session()

if settings.is_debug:
    logger.setLevel(logging.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    logger.setLevel(logging.WARNING)


@app.middleware("http")
async def middleware_all_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.debug(f'process_time: {round(process_time)} seconds')
    return response

from api.v1.others.router import router as utils_router
app.mount("/swagger-static", StaticFiles(directory="api/v1/others/static"))
app.include_router(utils_router, tags=["Others"])

from api.v1.user_subscriptions import router as user_subscriptions
app.include_router(user_subscriptions, prefix="/api/v1/user-subscription", tags=["User Subscriptions"])


if __name__ == "__main__":
    if settings.is_debug:
        import logging
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    uvicorn.run(app, host="0.0.0.0", port=8000)
