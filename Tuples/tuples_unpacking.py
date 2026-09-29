user = ("John Doe"  , 27 , "Developer")
name , age , role = user
print(name)


numbers = (1, 2, 3, 4, 5)
first , *middle , last = numbers

print(first)
print(middle)
print(last)


tuple = (1, 3, 7, 3, 8)

print(tuple.count(3))
print(tuple.index(7))