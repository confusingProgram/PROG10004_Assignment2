"""This module contains the User class, and its data fields"""

# User should have name, email, and address
class User():
    def __init__(self, username, email, address):
        self._username = username
        self._email = email
        self._address = address

    def get_username(self):
        return self._username
    
    def set_username(self, new_username):
        self._username = new_username

    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email

    def get_address(self):
        return self._address
    
    def set_address(self, new_address):
        self._address = new_address
"""
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, new_name):
        self._username = new_name

    @property
    def email(self):
        return self._email
    @email.setter
    def set_email(self, new_email):
        self._email = new_email

    @property
    def address(self):
        return str(self._address)
    @address.setter
    def address(self, new_address):
        self._address = new_address
"""