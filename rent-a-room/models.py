from sqlmodel import Field, SQLModel
class Room(SQLModel,table=True,primary_key=True):
    __tablename__: str = "rooms"
    id:int | None
    name: str = Field()
    price_per_night: int = Field()
    bedrooms: float = Field(multiple_of=0.5)
    bathrooms: float = Field(multiple_of=0.5)
Room()
