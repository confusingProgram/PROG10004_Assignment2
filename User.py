"""This module contains the User class, and its data fields"""

# User should have name, email, and address
class User():
    def __init__(self, user, email, address):
        self._username = user
        self._email = email
        self._address = address

    def get_name(self):
        return self._username
    
    def set_name(self, new_name):
        self._username = new_name

    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email

    def get_address(self):
        return self._address

    def set_address(self, new_address):
        self._address = new_address
