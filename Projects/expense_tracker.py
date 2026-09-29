expense = {
    "Food" : 0,
    "Traveling" : 0
}

category = input("Enter Category: ")
amount = int(input("Enter Amount: "))

expense[category] = expense.get(category,0) + amount
print(expense)