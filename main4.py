from database import Admin

try:
    Admin_name = input("Enter name\n")
    Admin_email = input("Enter email\n")
    Admin_password = input("Enter password\n")
    Admin_role = input("Enter role\n")
    Admin_permissions = input("Enter permissions\n")
    Admin.create(name=admin_name,email=admin_email,password=admin_password,role=admin_role,permissions=admin_permissions)

    print("Data is saved ")
except:
    print("404 error")