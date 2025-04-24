from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from database import create_tables
from app.router import router as url_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager to handle application lifespan events.

    This function is called when the application starts and stops.
    It creates the necessary database tables when the application is started.
    """
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(url_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True)
