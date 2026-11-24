phonebook = {
    "Pizza Palace": "12345678",
    "Mia's Bakery": "23456789",
    "City Flowers": "34567890",
    "Quick Clean": "45678901",
    "Happy Pets": "56789012"
}

business_name = input("Enter a business name: ")
phone_number = input("Enter the phone number: ")

phonebook[business_name] = phone_number

search_name = input("Enter a business name to look up: ")
print(phonebook[search_name])

print(phonebook)
print(phonebook.keys())