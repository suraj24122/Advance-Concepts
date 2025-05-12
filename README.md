# 🐍 Python Basics Practice Programs (Beginner Friendly)

Welcome to a collection of simple and beginner-friendly Python programs designed to help you understand core concepts like **getters/setters**, **static methods**, **decorators**, **exception handling**, and more — all explained in a fun, cartoon-style way! 🌈

---

## 📚 Topics Covered

1. [Getters and Setters](#-1-getters-and-setters)
2. [Static and Class Methods](#-2-static-and-class-methods)
3. [Decorators](#-3-decorators)
4. [Magic/Dunder Methods](#-4-magicdunder-methods)
5. [Exception Handling & Custom Errors](#-5-exception-handling--custom-errors)
6. [Finally Block](#-6-finally-block)
7. [map(), filter(), reduce()](#-7-map-filter-reduce)

---

## 🔐 1. Getters and Setters

**Practice 1**
```python
class Student:
    def __init__(self):
        self._name = ""

    def get_name(self):
        return self._name

class BankAccount:
    def __init__(self):
        self._balance = 0

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount

    def get_balance(self):
        return self._balance

acc = BankAccount()
acc.set_balance(1000)
print(acc.get_balance())

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))

class Animal:
    species = "Dog"

    @classmethod
    def get_species(cls):
        return cls.species

print(Animal.get_species())

✨ 3. Decorators
Practice 1
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

def upper_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@upper_decorator
def greet():
    return "good morning"

print(greet())

🪄 4. Magic/Dunder Methods
Practice 1

python
Copy
Edit
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python Basics")
print(b)
Practice 2

python
Copy
Edit
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)
🧯 5. Exception Handling & Custom Errors
Basic try-except

python
Copy
Edit
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("That’s not a number!")
Custom Error

python
Copy
Edit
class TooSmallError(Exception):
    pass

try:
    age = 3
    if age < 5:
        raise TooSmallError("Too young to play!")
except TooSmallError as e:
    print(e)
🧼 6. Finally Block
Practice 1

python
Copy
Edit
try:
    print(10 / 0)
except:
    print("Error happened!")
finally:
    print("Always runs!")
Practice 2

python
Copy
Edit
try:
    x = "hello"
    print(int(x))
except:
    print("Conversion failed.")
finally:
    print("Done trying!")
🛠 7. map(), filter(), reduce()
map() Example

python
Copy
Edit
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)
filter() Example

python
Copy
Edit
nums = [10, 15, 20, 25]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
reduce() Example

python
Copy
Edit
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)
🚀 How to Run
Clone this repo or copy the code snippets.

Use any Python IDE (e.g., VSCode, PyCharm, or Thonny).

Run and test each program for practice and learning.

🙌 About
Made with ❤️ by Suraj Singh — Connect on LinkedIn
This repo is part of my Python learning journey. Feel free to star ⭐ and share if it helped you!

yaml
Copy
Edit

---

Let me know if you'd like help organizing the code files for each concept into fold

    def set_name(self, name):
        self._name = name

s1 = Student()
s1.set_name("Suraj")
print(s1.get_name())


✅ Walrus Operator (:=)

✅ *args

✅ **kwargs

markdown
Copy
Edit
# 🐍 Python Special Features: Walrus Operator, *args, **kwargs

This repo contains simple and beginner-friendly Python programs that demonstrate:
- The 🦦 **Walrus Operator (`:=`)**
- The 🧸 `*args` (arbitrary arguments)
- The 🍬 `**kwargs` (keyword arguments)

All examples are explained in a way even school kids can understand! 🎓

---

## 🦦 1. Walrus Operator (`:=`)

### ✅ What it does:
Assigns a value and uses it at the same time (saves one line).

### 📄 Example 1:
```python
# Normal way
name = input("What's your name? ")
print("Hello", name)
python
Copy
Edit
# Walrus way
print("Hello", name := input("What's your name? "))
📄 Example 2:
python
Copy
Edit
if (n := 10) > 5:
    print("The number is big:", n)
🧺 2. *args – Many Unnamed Arguments
✅ What it does:
Allows you to pass many values to a function (like a bag of toys 🧸)

📄 Example 1:
python
Copy
Edit
def show_toys(*args):
    for toy in args:
        print("Toy:", toy)

show_toys("car", "doll", "ball")
📄 Example 2:
python
Copy
Edit
def add_numbers(*args):
    total = sum(args)
    print("Total is:", total)

add_numbers(1, 2, 3, 4)
🍭 3. **kwargs – Many Named Arguments
✅ What it does:
Lets you send values with names, like a dictionary (like labeled snacks 🍪)

📄 Example 1:
python
Copy
Edit
def show_snacks(**kwargs):
    for item, quantity in kwargs.items():
        print(f"{quantity} x {item}")

show_snacks(cookie=2, juice=1, candy=3)
📄 Example 2:
python
Copy
Edit
def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Suraj", age=20, grade="A")
🛠 How to Run
Copy and paste each example into a .py file.

Use any Python IDE (like VS Code or Thonny).

Run and play with the inputs to learn better.

🧠 Summary Table
Feature	Symbol	Use Case
Walrus Operator	:=	Assign + Use in same line
*args	*	Pass many unnamed values
**kwargs	**	Pass many named key=value values

🙌 Made by Suraj Singh
📘 Connect with me on LinkedIn
🌟 If you like it, please star ⭐ the repo and share it with friends!

yaml
Copy
Edit

---

You can paste this into your `README.md` on GitHub. Want help creating a nice folder 
