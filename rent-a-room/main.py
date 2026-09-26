from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="Rent a Room API",
    description="Book a stay in house or Room",
    version="1.0.0",
    contact={
        "name": "Test Enterprise LTD",
        "email": "test@example.com"
    }
)


# ---------------------------------------------------------
# Room Data
# ---------------------------------------------------------

apartment = {
    "id": 1,
    "name": "Sunny 2-bedroom apartment",
    "price_per_night": 200,
    "bedrooms": 2,
    "bathrooms": 1.5
}

house = {
    "id": 2,
    "name": "Cozy 1.5-bedroom apartment",
    "price_per_night": 350,
    "bedrooms": 1.5,
    "bathrooms": 1.5
}

studio = {
    "id": 3,
    "name": "Sunny 2-bedroom apartment",
    "price_per_night": 100,
    "bedrooms": 1,
    "bathrooms": 1
}


# ---------------------------------------------------------
# Query Parameter Model
# ---------------------------------------------------------

class RoomQueryParam(BaseModel):

    max_price: int | None = Field(
        default=None,
        ge=10,
        le=10_000
    )

    search: str | None = Field(
        default=None,
        min_length=3,
        max_length=10,
        title="Search Term",
        description="Provide a keyword to look for within the room's title"
    )

    @field_validator("search")
    @classmethod
    def fail_if_funny(cls, search: str | None):

        if search and "lol" in search.lower():
            raise ValueError("No funny business allowed")

        return search


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get(
    "/",
    status_code=status.HTTP_200_OK
)
def root():

    return {
        "message": "Welcome to Rent a rooms"
    }


# ---------------------------------------------------------
# Get All Rooms / Filter Rooms
# ---------------------------------------------------------

@app.get(
    "/rooms",
    status_code=status.HTTP_200_OK
)
def get_rooms(
    params: Annotated[RoomQueryParam, Query()]
):

    # Start with all rooms
    results = [apartment, house, studio]

    # Filter by maximum price
    if params.max_price is not None:

        results = [
            room
            for room in results
            if room["price_per_night"] <= params.max_price
        ]

    # Filter by search term
    if params.search:

        results = [
            room
            for room in results
            if params.search.lower() in room["name"].lower()
        ]

    return results


# ---------------------------------------------------------
# Get Mansions
# ---------------------------------------------------------

@app.get(
    "/rooms/mansions",
    status_code=status.HTTP_200_OK
)
def get_mansions(
    params: Annotated[RoomQueryParam, Query()]
):

    # Currently house is considered as a mansion
    results = [house]

    # Filter by maximum price
    if params.max_price is not None:

        results = [
            room
            for room in results
            if room["price_per_night"] <= params.max_price
        ]

    # Filter by search term
    if params.search:

        results = [
            room
            for room in results
            if params.search.lower() in room["name"].lower()
        ]

    return results


# ---------------------------------------------------------
# Get Room By ID
# ---------------------------------------------------------

@app.get(
    "/rooms/{room_id}",
    status_code=status.HTTP_200_OK
)
def get_room(room_id: int):

    for room in [apartment, house, studio]:

        if room["id"] == room_id:
            return room

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Room not found"
    )
