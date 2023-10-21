"""This module contains the Application, where the program will interact with the user"""
from User import User
from Pizza import Pizza

# Placeholder values for information to get from user.
username = ""
email = ""
address = ""
size = ""
number_of_pizzas = 0
confirm = ""

# Welcome text
print("Stackables: The Best Pizza Around".center(100, " "))
print()
print("Thank you for using our service!")

while True: # User information loop
    username = input("Enter your name: ")
    email = input("Enter your email address: ")
    address = input("Enter the delivery address: ")

    while True: # Confirmation loop
        print("Your name is: " + username)
        print("Your email address is: " + email)
        print("The delivery address is: " + address)
        confirm = input("Is this correct? Yes or No: ")

        if confirm == "Yes" or confirm == "No": # Confirmation loop will break if "Yes" or "No"
            break
        else:
            print("Please select Yes or No.")
    print()
        
    if confirm == "Yes": # User info loop will end if confirmation is "Yes"
        print("Welcome " + username + "!")
        break

while True: # Pizza size selection
    size = input("What size pizza would you like? Small, Medium, Large, or X-Large: ")
    if size == "Small":
        print("Price per Small pizza: $10.")
    elif size == "Medium":
        print("Price per Medium pizza: $12")
    elif size == "Large":
        print("Price per Large pizza: $15")
    elif size == "X-Large":
        print("Price per X-Large pizza: $18")
    else:
        print("Please enter a proper size.")
        continue
    
    while True:
        confirm = input("Are you sure you want " + size + " size? Yes or No: ")
        if confirm == "Yes" or confirm == "No":
            break
        else:
            print("Please select Yes or No.")
    
    print()
    
    if confirm == "Yes":
        print(size + " size selected.")
        break

while True: # Pizza number selection
    number_of_pizzas = input("How many pizzas would you like: ")
    if number_of_pizzas.isdigit() == False or number_of_pizzas == "0": # If number entered is negative, float, or 0
        print("Please enter a positive non-zero integer.")
        continue

    while True:
        confirm = input("Are you sure you want " + number_of_pizzas + "? Yes or No: ")
        if confirm == "Yes" or confirm == "No":
            break
        else:
            print("Please select Yes or No.")
    
    print()
    
    if confirm == "Yes":
        number_of_pizzas = int(number_of_pizzas)
        break

u1 = User(username, email, address)
p1 = Pizza(size, number_of_pizzas)

print("You have ordered " + str(p1) + ".")
print("Your total after the discount is $" + str(p1.total()) + ".")
print("Order will be delivered to " + u1.get_name + " at " + u1.get_address + ".")
print("Receipt will be emailed to " + u1.get_email)
print("Thank you for your service. Your order will arrive soon!")