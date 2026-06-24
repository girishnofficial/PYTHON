#GETTERS AND SETTERS,OVERLOADING,OVER RIDDING,ABSTARCT
# GETTERS AND SETTERS EXAMPLE

class Student:
    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

# Creating object
s1 = Student("Amit", 20)

# Using getter
print(s1.get_name())
print(s1.get_age())

# Using setter
s1.set_name("Rahul") # we can set new person or we get defalut user what we created befour
s1.set_age(22)

print(s1.get_name())
print(s1.get_age())


#method overloading
class Phone:
    def call(self, contact=None):
        if contact == "number":
            print("Calling using number...")
        elif contact == "video":
            print("Starting video call...")
        else:
            print("Calling default contact...")

p = Phone()

p.call("number")
p.call("video")
p.call()


#over ridding
class TV:
    def power(self):
        print("TV is ON")

class SmartTV(TV):
    def power(self):
        print("Smart TV is ON with apps loading")

t = SmartTV()
t.power()


from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Bank(ABC):

    @abstractmethod
    def interest(self):
        pass   # only rule, no implementation


# CHILD CLASS 1
class SavingsAccount(Bank):
    def interest(self):
        print("Savings interest = 5%")


# CHILD CLASS 2
class CurrentAccount(Bank):
    def interest(self):
        print("Current account = 0% interest")


# Objects
s = SavingsAccount()
c = CurrentAccount()

s.interest()
c.interest()

#menue driven program
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        print("Name:", self.name)
        print("Age :", self.age)


# Object
s = Student()

while True:
    print("\n--- MENU ---")
    print("1. Enter Student Data")
    print("2. Show Student Data")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        s.set_data(name, age)
        print("Data saved!")

    elif choice == 2:
        s.get_data()

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")


"""
What I Learned

In these lessons, I expanded my understanding of advanced Object-Oriented Programming (OOP) concepts and learned how to design interactive, user-friendly applications using menu-driven programming. These topics helped me understand how professional software systems are structured to ensure scalability, maintainability, and controlled access to data.

I explored getters and setters, which provide a secure way to access and modify private class attributes while maintaining data validation and encapsulation. I also learned how Python handles method overloading using default parameter values and how method overriding allows child classes to redefine behaviors inherited from parent classes.

Additionally, I studied the "super()" function, which enables child classes to access methods and constructors from their parent classes, promoting code reuse and extending functionality. I was also introduced to Abstract Base Classes (ABC), which act as blueprints for other classes and enforce the implementation of required methods, ensuring consistency across large applications.

Beyond OOP, I learned how to build menu-driven programs using loops, conditional statements, and functions. I practiced creating interactive applications such as a calculator and a banking system, where users can select options from a menu and perform different operations. These projects demonstrated how to combine programming fundamentals to create structured and user-friendly command-line applications.

Overall, these lessons strengthened my software design skills and provided practical experience in building modular, reusable, and interactive Python programs.

Concepts Covered

Advanced OOP Concepts

- Getters and Setters
- Data Encapsulation
- Private Attributes ("__attribute")
- Data Validation

Method Handling

- Method Overloading (using Default Parameters)
- Method Overriding
- Extending Parent Class Functionality

Inheritance Utilities

- "super()" Function
- Parent and Child Class Interaction
- Constructor Reuse

Abstract Classes

- Abstract Base Classes (ABC)
- Abstract Methods
- Interface Enforcement
- Blueprint-Based Design

Menu-Driven Programming

- Interactive Command-Line Applications
- User Menu Systems
- Program Navigation

Control Flow and Program Structure

- "while True" Loops
- "if", "elif", and "else"
- Functions and Modular Programming
- DRY (Don't Repeat Yourself) Principle

Practical Applications

- Calculator Application
- Banking System Simulation
- Balance Management
- User Input Validation
- Persistent Program State

Key Takeaways

- Learned how getters and setters improve data security and validation.
- Understood the importance of encapsulation in protecting object data.
- Explored method overloading techniques available in Python.
- Applied method overriding to customize inherited behavior.
- Used the "super()" function to reuse and extend parent class functionality.
- Learned how abstract classes enforce consistent class structures.
- Built interactive menu-driven programs using loops and conditional statements.
- Improved code organization through modular programming with functions.
- Applied the DRY principle to reduce code repetition and improve maintainability.
- Developed practical problem-solving skills through calculator and banking system projects.
- Strengthened my understanding of advanced OOP concepts used in real-world software development.
- Gained experience designing scalable and user-friendly Python applications.
"""