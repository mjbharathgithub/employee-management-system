from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import  Session
from database import SessionLocal, EmployeeDB
from model import Employee, EmpoloyeeUpdate, EmployeeResponse


app = FastAPI(
    title="Employee Management System",
    description="API for managing employee records",
    version="1.0.0"
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        


# API Endpoints

#Create Employee
@app.post("/employees/",response_model=EmployeeResponse,status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee, db: Session = Depends(get_db)):
    db_employee = EmployeeDB(**employee.dict())

    try:
        print("employee_Details : ",db_employee)
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)


    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists or invalid data"
        )
    
    return db_employee

@app.get("/employees/{employee_id}",response_model=EmployeeResponse)
def get_Employee_By_ID(employee_id:int,db:Session=Depends(get_db)):
    employee=db.query(EmployeeDB).filter(EmployeeDB.id==employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee is not found for the given ID"
        )
    
    return employee

@app.get("/employees/", response_model=List[EmployeeResponse])
def read_employees( db: Session = Depends(get_db)):
    employees = db.query(EmployeeDB).all()
    return employees

@app.put("/employees/{employee_id}",response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmpoloyeeUpdate, db: Session= Depends(get_db)):
    db_employee = db.query(EmployeeDB).filter(EmployeeDB.id== employee_id).first()

    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Failed to update Employee since ID not found...."
        )

    if employee.name is not None:
        db_employee.name = employee.name
    if employee.email is not None:
        db_employee.email = employee.email
    if employee.position is not None:
        db_employee.position = employee.position
    if employee.salary is not None:
        db_employee.salary = employee.salary


        db.commit()
        db.refresh(db_employee)
    
        

    return db_employee

@app.delete("/employees/{employee_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id:int, db:Session=Depends(get_db)):
    employee=db.query(EmployeeDB).filter(EmployeeDB.id==employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Failed to Delete since Employee not found"
        )
    try:
        db.delete(employee)
        db.commit()
    except Exception:
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting employee"
        )
    return {"ok": True}




