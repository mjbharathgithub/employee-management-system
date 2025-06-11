import requests
import json

BASE_URL = "http://localhost:8000"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print(response.text)

def create_employee():
    name = input("Enter employee name: ")
    email = input("Enter employee email: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    url = f"{BASE_URL}/employees/"
    data = {
        "name": name,
        "email": email,
        "position": position,
        "salary": salary
    }

    print(f"\nCreating employee: {name}")
    response = requests.post(url, json=data)
    print_response(response)

def viewEmployeeByID():
    employee_id=int(input("Enter Employee ID: "))
    url = f"{BASE_URL}/employees/{employee_id}"
    print(f"\nGetting employee with ID: {employee_id}")
    response = requests.get(url)
    print_response(response)

def viewAllEmployees():
    url = f"{BASE_URL}/employees/"
    print("\nGetting all employees...")
    response = requests.get(url)
    print_response(response)

def updateEmployeeByID():
    employee_id = int(input("Enter Empoyee ID to update: "))

    name = input("Enter new Name (leave blank to keep unchanged): ")
    email = input("Enter new Email (leave blank to keep unchanged): ")
    position = input("Enter new Position (leave blank to keep unchanged): ")
    salary = input("Enter new Salary (leave blank to keep unchanged): ")

    data = {}
    if name:
        data["name"] = name
    if email:
        data["email"] = email
    if position:
        data["position"] = position
    if salary:
        try:
            data["salary"] = float(salary)
        except ValueError:
            print("Invalid salary. Please enter a numeric value.")
            return

    if not data:
        print("\nNo data provided to update.")
        return

    url = f"{BASE_URL}/employees/{employee_id}"
    print(f"\nUpdating employee with ID: {employee_id}...")
    
    response = requests.put(url, json=data)
    print_response(response)


def deleteEmployeeByID():
    employee_id=int(input("Enter Employee ID: "))
    url=f"{BASE_URL}/employees/{employee_id}"
    print(f"\nDeleting Employee with ID: {employee_id}")

    response=requests.delete(url)
    print(response)




def main():

    while True:
        print('''----Employee Mangement System----
              1.Create Employee
              2.View Employee by ID
              3.View all Employees
              4.Update Employee by ID
              5.Delete Employee by ID
              0.Exit
              >>''')
        option=input("Enter your option: ")

        if option=='1':
            create_employee()

        elif option=='2':
            viewEmployeeByID()

        elif option=='3':
            viewAllEmployees()

        elif option=='4':
            updateEmployeeByID()

        elif option=='5':
            deleteEmployeeByID()
        
        else:
            print("Exiting Employee Mangement System...")
            break


if __name__=="__main__":
    main()
