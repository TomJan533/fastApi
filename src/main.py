from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from src.routers import example, sections
from src.models import Base
from src.db import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield

    await engine.dispose()


app = FastAPI(
    title="FastAPI base project",
    description="This is a base project built with FastAPI.",
    version="1.0.0",
    contact={
        "name": "tomaszj",
    },
    lifespan=lifespan,
)


app.include_router(example.router)
app.include_router(sections.router)


@app.get("/", include_in_schema=False)
async def redirect_to_example():
    return RedirectResponse(url="/example")
