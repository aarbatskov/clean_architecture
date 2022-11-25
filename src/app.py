from fastapi import FastAPI
from routing.books import router as books_routing

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(books_routing)
