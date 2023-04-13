from database import Employee

employees = Employee.select()
for employee in employees:
    print(employee.name,employee.email,employee.password)