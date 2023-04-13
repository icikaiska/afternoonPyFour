from database import Employee

try:
    employee_name = input("Enter name\n")
    employee_email = input("Enter email\n")
    employee_password = input("Enter password\n")
    employee.create(name=employee_name,email=employee_email,password=employee_password)

    print("Employee data saved succesfully")
except:
    print("Incorrect username or password")