from sqlmodel import Session, create_engine, SQLModel
from models import Room

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
    echo=True
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session 
# Request is going to hit a Route Handeler
# Route handller is having dependency on get session
# get_session will create  a database session
# get session will yield/cede control to the route handeller
# route handeler will finish up
#    