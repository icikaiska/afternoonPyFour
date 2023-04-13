from database import Product
try:
    p_name = input("Enter product name\n")
    p_qqty = input("Enter product quantity\n")
    p_price = input("Enter product price\n")
    Product.create(name=p_name,qtty = p_qqty, price=p_price)
    print("Product saved successfully")

except:
    print("Error occured")