# 🐍 Python Programming – Stage 4: Data Structures

## 📌 Overview

This stage focuses on **Python Data Structures**, which are used to store, organize, and manipulate data efficiently. Understanding these concepts is essential for building real-world applications like management systems, trackers, and data-driven programs.

---

# 🎯 Goal

Learn how to:

* Store collections of data
* Access and modify data efficiently
* Choose the right data structure for the right problem

---

# 🟡 1. Lists

## 📖 Description

Lists are **ordered and mutable (changeable)** collections.

## ✅ Creating Lists

```python
nums = [10, 20, 30]
mixed = [10, "hello", 3.5]
```

## 🔍 Accessing Elements

```python
print(nums[0])   # first element
print(nums[-1])  # last element
```

## ✏️ Modifying Data

```python
nums[1] = 50
```

## 🔃 Sorting

```python
nums.sort()
nums.sort(reverse=True)
```

## 🔎 Searching

```python
if 20 in nums:
    print("Found")

nums.index(20)
```

## ⚙️ List Methods

* `append()` → add element
* `insert()` → add at position
* `remove()` → remove value
* `pop()` → remove last element
* `clear()` → remove all elements
* `len()` → get length

## ⚡ List Comprehension

```python
squares = [x*x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```

---

# 🟡 2. Tuples

## 📖 Description

Tuples are **ordered but immutable (unchangeable)** collections.

## ✅ Creating Tuples

```python
t = (10, 20, 30)
single = (5,)
```

## 🔍 Accessing Data

```python
print(t[1])
```

## 🎁 Tuple Unpacking

```python
a, b, c = (1, 2, 3)
```

## 📌 When to Use

* Fixed data
* Faster performance
* Prevent accidental modification

---

# 🟡 3. Sets

## 📖 Description

Sets store **unique values** and do not allow duplicates.

## ✅ Creating Sets

```python
s = {1, 2, 2, 3}
```

## ➕ Adding Values

```python
s.add(5)
```

## ❌ Removing Values

```python
s.remove(2)
s.discard(10)
```

## 🔗 Set Operations

```python
a = {1,2,3}
b = {3,4,5}

a | b   # union
a & b   # intersection
a - b   # difference
```

---

# 🟡 4. Dictionaries

## 📖 Description

Dictionaries store data in **key-value pairs**.

## ✅ Creating Dictionary

```python
student = {
    "name": "Shruu",
    "age": 20
}
```

## ➕ Adding Data

```python
student["marks"] = 90
```

## ✏️ Updating Data

```python
student["age"] = 21
```

## ❌ Removing Data

```python
student.pop("age")
del student["name"]
```

## 🧩 Nested Dictionaries

```python
students = {
    "101": {"name": "A", "marks": 80},
    "102": {"name": "B", "marks": 90}
}
```

## ⚙️ Dictionary Methods

* `keys()` → get all keys
* `values()` → get all values
* `items()` → key-value pairs
* `get()` → safe access

## ⚡ Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
```

---

# 🧠 Data Structure Comparison

| Type       | Ordered | Mutable | Duplicates  | Syntax      |
| ---------- | ------- | ------- | ----------- | ----------- |
| List       | Yes     | Yes     | Yes         | [ ]         |
| Tuple      | Yes     | No      | Yes         | ( )         |
| Set        | No      | Yes     | No          | { }         |
| Dictionary | Yes     | Yes     | Keys unique | {key:value} |

---

# 🧪 Practice Ideas

* Store numbers and find max/min
* Remove duplicates using set
* Create and update student records
* Build dictionary-based programs

---

# 🚀 Mini Projects

## 📞 Contact Management System

Store and manage contacts using dictionaries.

## 🎓 Student Management System

Store student data with nested dictionaries.

## 📝 To-Do List

Manage tasks using lists.

## 📦 Inventory Management System

Track items and quantities using dictionaries.

## 💸 Expense Tracker

Store and update expenses by category.

---

# ▶️ How to Run

1. Install Python
2. Open project folder in VS Code
3. Run any file:

```bash
python filename.py
```

---

# 💡 Key Takeaways

* Lists are flexible and commonly used
* Tuples protect fixed data
* Sets remove duplicates automatically
* Dictionaries are powerful for real-world data

---

# 📈 Next Step

After mastering this stage:

* Learn Functions
* Learn File Handling
* Build complete applications

---

# ⭐ Final Note

Mastering data structures is a turning point in your programming journey. These concepts are used in almost every real-world application.

Practice consistently and build small projects to strengthen your understanding 🚀
