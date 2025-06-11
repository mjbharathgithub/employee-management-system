from pydantic import BaseModel
from typing import Optional

# Pydantic model for creating an employee
class Employee(BaseModel):
    name: str
    email: str
    position: str
    salary: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Joseph Bharath",
                "email": "jseohph@example.com",
                "position": "Software Engineer",
                "salary": 75000.0
            }
        }

# Pydantic model for updating an employee
class EmpoloyeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None

# Pydantic model for the response
class EmployeeResponse(Employee):
    id: int

    class Config:
        orm_mode = True
