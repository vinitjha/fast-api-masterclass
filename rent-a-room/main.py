from sqlmodel import Session, select

from database import engine, create_db_and_tables
from models import Room

from contextlib import asynccontextmanager

from fastapi import FastAPI


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


@app.get("/rooms")
def get_rooms():

    with Session(engine) as session:

        statement = select(Room)

        rooms = session.exec(statement).all()

        return rooms