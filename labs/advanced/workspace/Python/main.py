from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Disney Movies API",
    description="RESTful API for managing Disney movie data with full CRUD operations",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Include router
app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    """Root endpoint providing API information."""
    return {
        "message": "Disney Movies API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

