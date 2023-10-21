"""This module contains the Pizza class, its data fields, and its methods"""

class Pizza():
    """This class is the Pizza class, which contains its data fields and its methods"""
    def __init__(self, size, number_of_pizzas):
        """The initialization method, reads size of pizza(s), and number of pizzas, and sets the size, number of pizzas, and price."""
        self.size = size # Sizes are restricted to Small, Medium, Large, and X-large
        self.price = 0 # Prices are restricted to $10, 12, 15, and 18 per pizza, depending on size.
        self.number_of_pizzas = number_of_pizzas

        if self.size == "Small": # Price per pizza is dependant on the size ordered
            self.price = 10
        elif self.size == "Medium":
            self.price = 12
        elif self.size == "Large":
            self.price = 15
        elif self.size == "X-Large":
            self.price = 18

    def total(self):
        """The total method, calculates the total dollar amount for the order."""
        total = self.price * self.number_of_pizzas # Setting total to price * number of pizzas
        if self.number_of_pizzas >= 3: # If there are 3 or more pizzas, apply a 15% discount, and round
            total = total *0.85 # Discount
            total = total * 100 // 1 # Rounding to 2 cent places
            total = total / 100

        total = float(total) # total is converted to float in case total is something like #10 -> $10.0
        total = str(total) # total is converted to string in order to create two decimal places in case of something like $10.0 -> $10.00
        array = total.split(".")
        if len(array[1]) == 1: # If the decimal part of the number contains only 1 number in the case it is a multiple of 10 (0, 10, 20, etc.), it will create an extra 0.
            total = total + "0"
        return total
    
    def __str__(self):
        """The string method, returns the object information as a string"""
        string = str(self.number_of_pizzas) + " " + self.size + " pizza"
        if self.number_of_pizzas > 1: # If number_of_pizzas ordered is greater than 1, the string is changed to include an s for display purposes.
            string = string + "s"
        return string