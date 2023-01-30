from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = (
    "postgresql://postgres:mysecredpassword@localhost:5432/py-mediatr"
)

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
