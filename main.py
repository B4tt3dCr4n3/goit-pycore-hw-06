'''
Create a sistem to store contacts in the address book.
'''

from collections import UserDict

class Field:
    '''
    Base class for all fields.
    '''
    def __init__(self, value): # Initialize the field with a value.
        self.value = value # Set the value of the field.

    def __str__(self): # Return the string representation of the field.
        return str(self.value) # Return the value of the field.

class Name(Field):
    # Initialize the Class with a value.
        pass

class Phone(Field):
    # Initialize the Class with a value.
		pass

class Record:
    '''
    Class to store a contact record.
    '''
    def __init__(self, name): # Initialize the record with a name.
        self.name = Name(name) # Set the name of the record.
        self.phones = [] # Initialize the list of phones.

    def add_phone(self, phone):
        '''
        Add a phone to the record.
        '''
        if self._is_valid_phone_number(phone): # Check if the phone number is valid.
            self.phones.append(Phone(phone)) # Add the phone to the list of phones.
        else: # If the phone number is not valid.
            print("Phone number should contain 10 digits.") # Print an error message.

    def edit_phone(self, old_phone, new_phone):
        '''
        Edit a phone in the record.
        '''
        if not self._is_valid_phone_number(new_phone): # Check if the new phone number is valid.
            print("Phone number should contain 10 digits.") # Print an error message.

        else: # If the new phone number is valid.
            for phone in self.phones: # Iterate over the list of phones.
                if phone.value == old_phone: # If the phone number is found.
                    phone.value = new_phone # Update the phone number.

    def find_phone(self, phone):
        '''
        Find a phone in the record.
        '''
        for p in self.phones: # Iterate over the list of phones.
            if p.value == phone: # If the phone number is found.
                return p.value # Return the phone number.
        return None # Return None if the phone number is not found.

    def _is_valid_phone_number(self, phone):
        '''
        Check if the phone number is valid.
        '''
        return isinstance(phone, str) and phone.isdigit() and len(phone) == 10
    # Return True if the phone number is valid.

    def __str__(self):
        '''
        Return the string representation of the record.
        '''
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}" # Return the name and phones of the record.

class AddressBook(UserDict):
    '''
    Class to store the address book.
    '''
    def add_record(self, record):
        '''
        Add a record to the address book.
        '''
        self.data[record.name.value] = record # Add the record to the data dictionary.

    def delete(self, name):
        '''
        Delete a record from the address book.
        '''
        return self.data.pop(name) # Remove the record from the data dictionary.

    def find(self, name):
        '''
        Find a record in the address book.
        '''
        return self.data.get(name) # Return the record from the data dictionary.

book = AddressBook() # Create an instance of the AddressBook class.

john_record = Record("John") # Create a record for John.
john_record.add_phone("1234567890") # Add a phone to the record.
john_record.add_phone("5555555555") # Add another phone to the record.

book.add_record(john_record) # Add the record to the address book.

jane_record = Record("Jane") # Create a record for Jane.
jane_record.add_phone("9876543210") # Add a phone to the record.
book.add_record(jane_record) # Add the record to the address book.

for name, record in book.data.items(): # Iterate over the records in the address book.
    print(record) # Print the record.

john = book.find("John") # Find the record for John.
john.edit_phone("1234567890", "1112223333") # Edit the phone number for John.

print(john) # Print the record for John.

found_phone = john.find_phone("5555555555") # Find a phone number for John.
print(f"{john.name}: {found_phone}") # Print the phone number.

book.delete("Jane") # Delete the record for Jane.
