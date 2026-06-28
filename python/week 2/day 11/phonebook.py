#1. Phonebook: Create a dict with 4 contacts (name → phone number).
#   Let user search by name and show number. If not found, say "Contact not found".
#   make it case-insensitive (i.e. "alice" should match "Alice").

phonebook={
    "Alice":"123-456-7890",
    "Bob":"987-654-3210",
    "Charlie":"555-1234",
    "Diana":"555-5678"
}

name=input("Enter name to search: ")
print(phonebook.get(name.capitalize(), "Contact not found!"))