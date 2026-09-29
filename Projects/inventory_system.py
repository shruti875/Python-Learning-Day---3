inventory = {
    "apple" : 10 ,
    "banana" : 15
}

item = input("enter item: ")
qty = int(input("Enter quantity of items: "))

inventory[item] = inventory.get(item , 0) + qty
print(inventory)
