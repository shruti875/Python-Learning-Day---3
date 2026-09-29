contact = {
    "adii" : 8850524457
}

# add contact 
name = input("enter name: ")
number = int(input("enter number: "))
contact[name] = number
print(contact)

# search 
search = input("Enter name you want to search: ")
print(contact.get(search , "not found"))
print(contact)

# delete
delete = input("Enter name you want to delete: ")
del contact[delete]
print(contact)