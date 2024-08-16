from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers import example

app = FastAPI(
    title="RAG Chat Api",
    description="This is a Retrieval Augumented Generation API built with FastAPI.",
    version="1.0.0",
    contact={
        "name": "tomaszj",
    },
)

app.include_router(example.router)


@app.get("/", include_in_schema=False)
async def redirect_to_example():
    """
    Redirect requests from the root path '/' to '/example'
    """
    return RedirectResponse(url="/example")
