from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker,declarative_base

# Creating Engine to connect to the DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./employees.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Creating EmployeeDB table structure
class EmployeeDB(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    position = Column(String(100))
    salary = Column(Float)

# Creating the employees table in the database
Base.metadata.create_all(bind=engine)
