from sqlmodel import Session

from database import engine
from models import Room


def create_rooms():

    with Session(engine) as session:

        apartment = Room(
            name="Sunny 2-bedroom apartment",
            price_per_night=200,
            bedrooms=2,
            bathrooms=1.5
        )

        house = Room(
            name="Cozy 3-bedroom house",
            price_per_night=350,
            bedrooms=3,
            bathrooms=2.5
        )

        studio = Room(
            name="Modern studio near museum",
            price_per_night=150,
            bedrooms=1,
            bathrooms=1
        )

        session.add(apartment)
        session.add(house)
        session.add(studio)

        session.commit()

        print("Rooms inserted successfully!")


if __name__ == "__main__":
    create_rooms()