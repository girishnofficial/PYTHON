#OOP (OBJECT-ORIENTED PROGRAMMING)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("mr bro", 20)

print(s1.name)
print(s1.age)


#multiple object diffrent attributes

class Laptop:
    def __init__(self, brand, processor, ram, storage, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.price = price


# Create an object
laptop1 = Laptop("Dell", "Intel i5", "8GB", "512GB SSD", 60000)

# Print details
print(laptop1.brand)
print(laptop1.processor)
print(laptop1.ram)
print(laptop1.storage)
print(laptop1.price)


"""MAIN PILLARS OF OOP (OBJECT-ORIENTED PROGRAMMING)

1. Encapsulation
- Wrapping data and methods into a single unit (class)
- Restricts direct access to data
- Helps in data hiding and security

2. Inheritance
- One class acquires properties of another class
- Helps in code reusability
- Example: Child class inherits from Parent class

3. Polymorphism
- One method behaves in different ways
- Same function name, different behavior
- Example: method overriding, method overloading

4. Abstraction
- Hides internal implementation details
- Shows only essential features to the user
- Helps in reducing complexity

SUMMARY:
Encapsulation → Data hiding
Inheritance   → Reusability
Polymorphism  → Many forms
Abstraction   → Hiding complexity"""


# 1. ENCAPSULATION
class Student:
    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age

    def get_details(self):
        return self.__name, self.__age

s1 = Student("Amit", 20)
print(s1.get_details())




# 2. INHERITANCE
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()


# 3. POLYMORPHISM
class Bird:
    def sound(self):
        print("Bird chirps")

class Dog:
    def sound(self):
        print("Dog barks")

for obj in [Bird(), Dog()]:
    obj.sound()



# 4. ABSTRACTION
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of Circle")

c = Circle()
c.area()


# SUPER FUNCTION EXAMPLE

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()   # calling parent class method
        print("This is Child class")

c = Child()
c.show()


"""
What I Learned

In these lessons, I explored Object-Oriented Programming (OOP) in Python, a programming paradigm that helps organize code into reusable and maintainable structures called classes and objects. I learned how OOP enables developers to model real-world entities, improve code organization, and build scalable applications.

I began by understanding classes, objects, constructors, and the "self" keyword. I learned how the "__init__()" constructor automatically initializes object attributes when an object is created and how "self" allows access to instance-specific data and methods. I also explored the difference between class variables and instance variables, as well as the use of optional parameters to create more flexible objects.

Additionally, I studied the four fundamental pillars of OOP: Abstraction, Encapsulation, Inheritance, and Polymorphism. I learned how abstraction hides implementation complexity while exposing only essential functionality, and how encapsulation protects data by restricting direct access through private attributes and controlled methods.

Furthermore, I explored inheritance, which allows child classes to reuse and extend functionality from parent classes, reducing code duplication and promoting reusability. I also learned about polymorphism, where different classes can share a common interface while implementing unique behaviors through method overriding.

These concepts provided a strong foundation for designing professional, modular, and scalable software systems.

Concepts Covered

OOP Fundamentals

- Classes and Objects
- Object Creation
- Constructors ("__init__()")
- The "self" Keyword
- Object Initialization

Variables and Scope

- Instance Variables
- Class Variables
- Optional Constructor Parameters

OOP Pillars

Abstraction

- Hiding Implementation Details
- Exposing Essential Features
- Simplifying User Interaction

Encapsulation

- Data Protection
- Private Attributes ("__variable")
- Controlled Access Through Methods

Inheritance

- Parent and Child Classes
- Code Reusability
- "super()" Method

Types of Inheritance

- Single Inheritance
- Multiple Inheritance
- Multi-Level Inheritance
- Hierarchical Inheritance

Polymorphism

- Method Overriding
- Common Interfaces
- Dynamic Behavior

Real-World Applications

- ATM Systems
- Database Management
- Notification Systems
- Animal Behavior Simulation
- User and Employee Models

Key Takeaways

- Learned how classes and objects help model real-world entities in software.
- Understood the role of constructors in initializing object data.
- Applied the "self" keyword to access instance-specific attributes and methods.
- Differentiated between class variables and instance variables.
- Explored abstraction to simplify complex systems for users.
- Learned how encapsulation improves security and data integrity.
- Used inheritance to reduce code duplication and improve reusability.
- Applied the "super()" method to extend parent class functionality.
- Understood different inheritance models used in software design.
- Implemented polymorphism through method overriding and shared interfaces.
- Strengthened software design skills by learning the four pillars of Object-Oriented Programming.
- Built a strong foundation for advanced Python development, backend frameworks, automation, and large-scale software applications.
"""