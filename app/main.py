from fastapi import FastAPI
from .routers import tickets, agents  # Import agents router
import asyncio
from .realtime import run_subscriber


async def app_lifespan(app: FastAPI):
    # Startup event
    asyncio.create_task(run_subscriber())
    yield


app = FastAPI(lifespan=app_lifespan)

app.include_router(tickets.router, prefix="/api")
app.include_router(agents.router, prefix="/api")  # Register the agents API
