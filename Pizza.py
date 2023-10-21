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