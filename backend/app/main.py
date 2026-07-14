from fastapi import FastAPI

from app.api.customers import router as customer_router
from app.core.config import get_settings
from app.core.exceptions import (
    BlinkAIException,
    blink_exception_handler,
)
from app.core.logging import configure_logging, logger

configure_logging()

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_exception_handler(
    BlinkAIException,
    blink_exception_handler,
)

app.include_router(customer_router)


@app.on_event("startup")
async def startup():
    logger.info("Blink AI started")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Blink AI stopped")


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
