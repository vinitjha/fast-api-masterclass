from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Creating database and tables...")

    create_db_and_tables()

    yield

    print("Application shutting down...")


app = FastAPI(
    lifespan=lifespan,
    title="Rent a Room API",
    description="Book a stay in a house or room",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Rent a Room API"
    }