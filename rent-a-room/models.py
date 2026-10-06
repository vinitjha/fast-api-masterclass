from sqlmodel import Field, SQLModel


class Room(SQLModel, table=True):
    __tablename__ = "rooms"

    id: int | None = Field(default=None, primary_key=True)

    name: str
    price_per_night: int
    bedrooms: float = Field(multiple_of=0.5)
    bathrooms: float = Field(multiple_of=0.5)