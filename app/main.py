from fastapi import FastAPI, HTTPException
from .routers import tickets, agents  # Import agents router
import asyncio
from .realtime import run_subscriber


async def app_lifespan(app: FastAPI):
    try:
        # Startup event
        asyncio.create_task(run_subscriber())
        yield
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred during app startup: {str(e)}"
        )


app = FastAPI(lifespan=app_lifespan)

try:
    app.include_router(tickets.router, prefix="/api")
    app.include_router(agents.router, prefix="/api")  # Register the agents API
except Exception as e:
    raise HTTPException(
        status_code=500, detail=f"An error occurred while including routers: {str(e)}"
    )
