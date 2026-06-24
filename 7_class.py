#functions [reuseble block of code] "def" mean defination
def greet():#always give def for any fuction
    print("hello")
greet()#greet() wecan give unlimited fuction
greet()
greet()
greet()
greet()
greet()# here total 6 greet() are ther so its gives 6 times hello


#fuction in parameter
# Function that will be passed as a parameter
def greet(name):
    return f"Hello, {name}!"

# Function that accepts another function as a parameter
def execute(func, value):
    # Call the function passed in 'func'
    return func(value)

# Passing 'greet' function as an argument
result = execute(greet, "mr bro")

print(result)



# or in simple way
def tables(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
tables(57)


#default parameter
def greet(name="Guest"):
    print("Hello", name)

greet()          # uses default value
greet("viwers")   # overrides default
greet("mrbro")



#return values from a function
def add(a, b):
    return a + b
result = add(3, 5)
print(result)


# global variable
x = 10   #out side of function
def show():
    print(x)
show()
print(x)


# local variable
def show():
    y = 5   #inside the fuction
    print(y)
show()


#variable lenght arguments[*]
def add(*numbers): #*is an argument symbole
    return sum (numbers)#what number we gives that adds
print(add(1,100,1)) # 100 + 1 + 1 = 102


# function with keyword arguments (**kwargs)
def st(**detail):
    for key, value in detail.items():
        print(f"{key} : {value}")

# calling the function
st(name="anand", age=22, course="python")


#lambda fuction

add=lambda a,b :a+b #adding values like 1+2=3
print(add(1,2))#3


#lambda in dictionary
students = {
    "s1": {"name": "Anand", "age": 22, "marks": 85},
    "s2": {"name": "Ravi", "age": 20, "marks": 78},
    "s3": {"name": "Kiran", "age": 23, "marks": 90}
}

# print all students
for key, value in students.items():
    print(key, value)



#recurtion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(3))


#nested def fuction
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

"""
What I Learned

In these lessons, I learned one of the most important concepts in Python programming: functions. Functions help organize code into reusable blocks, making programs more structured, maintainable, and efficient. By following the "Don't Repeat Yourself" (DRY) principle, functions reduce code duplication and improve readability.

I learned how to define and call functions using the "def" keyword, pass data through parameters and arguments, and use both positional and keyword arguments. I also explored default parameters, which allow functions to operate even when certain arguments are not provided.

Additionally, I gained an understanding of return values and how the "return" statement enables functions to send results back to the main program for further processing. I learned the difference between local and global variables and how variable scope affects accessibility within a program.

The lessons also introduced advanced function concepts, including variable-length arguments using "*args" and "**kwargs", which provide flexibility when handling an unknown number of inputs. I explored lambda functions for creating concise anonymous functions, recursion for solving problems through self-referencing function calls, and nested functions for improving code organization and modularity.

These concepts strengthened my ability to write cleaner, more reusable, and scalable Python programs while introducing programming techniques commonly used in real-world applications and data analysis workflows.

Concepts Covered

Functions

- Function Definition using "def"
- Function Calls
- Reusable Code Blocks
- DRY (Don't Repeat Yourself) Principle

Parameters and Arguments

- Positional Arguments
- Keyword Arguments
- Default Parameters

Return Values

- "return" Statement
- Returning Data from Functions
- Function Output Processing

Variable Scope

- Local Variables
- Global Variables
- Scope Management

Advanced Function Concepts

- Variable Length Arguments ("*args")
- Keyword Variable Arguments ("**kwargs")
- Lambda Functions
- Anonymous Functions

Recursion

- Recursive Functions
- Base Conditions
- Problem Decomposition

Nested Functions

- Functions Inside Functions
- Code Modularity
- Encapsulation of Logic

Key Takeaways

- Learned how functions improve code organization and reusability.
- Understood how to define, call, and manage functions effectively.
- Applied positional, keyword, and default arguments to create flexible functions.
- Used the "return" statement to pass results back to the main program.
- Learned the difference between local and global variables and their scope.
- Explored "*args" and "**kwargs" for handling dynamic inputs.
- Created concise operations using lambda functions.
- Understood recursion and the importance of base conditions in recursive programs.
- Applied nested functions to improve code structure and maintainability.
- Strengthened problem-solving and programming skills through modular coding practices.
- Built a strong foundation for advanced Python topics, data analysis, automation, and software development.
"""