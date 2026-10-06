from sqlmodel import create_engine,SQLModel
sqlite_file_name = "database.db"
sqllite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqllite_url,connect_args={"check_same_thread": False},echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)