from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    breed = Column(String(255))

def create_table():
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

# SQLite database URL (change this as needed)
SQLITE_URL = "sqlite:///my_database.db"
engine = create_engine(SQLITE_URL)
Session = sessionmaker(bind=engine)
session = Session()
