#ERROR AND EXCEPTION HANDLING
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    result = a / b

except:
    print("Something went wrong (invalid input or division error)")

else:
    print("Result:", result)

finally:
    print("Program finished")



#MULTIPLE Exception

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")

finally:
    print("Program finished")



# RAISING EXCEPTION

age = int(input("Enter age: "))

if age < 18:
    raise Exception("You are not eligible (Age must be 18 or above)")
else:
    print("You are eligible")



#file handling [r=read,w=write,a=append,r+=read + write]

# Read mode example ('r')

file = open("sample.txt", "r")

content = file.read()
print("File Content:")
print(content)

file.close()



# Write mode example ('w')

file = open("sample.txt", "w")

file.write("Hello! This is new content.\n")
file.write("Old data will be deleted.")

file.close()

print("Data written successfully!")



# Append mode example ('a')

file = open("sample.txt", "a")

file.write("\nThis line is added later.")
file.write("\nAnother new entry.")

file.close()

print("Data appended successfully!")


# Read + Write mode example ('r+')

file = open("sample.txt", "r+")

print("Current content:")
print(file.read())

# Move cursor to start
file.seek(0)

file.write("UPDATED TEXT\n")

file.close()

print("File updated using r+ mode!")




"""
What I Learned

In these lessons, I learned how to build interactive menu-driven applications, handle errors effectively, and work with files in Python. These concepts are essential for developing reliable, user-friendly, and real-world software applications.

I explored menu-driven programming, where users interact with a program through a set of options. By combining loops, conditional statements, and functions, I learned how to create structured command-line applications such as calculators and banking systems. I also understood the importance of modular programming and the DRY (Don't Repeat Yourself) principle for improving code readability and maintainability.

Additionally, I studied error and exception handling, which helps programs respond gracefully to unexpected situations instead of crashing. I learned the difference between syntax errors and runtime exceptions and practiced using the "try", "except", "else", and "finally" blocks to manage errors effectively. I also explored handling specific exceptions and creating custom exceptions using the "raise" keyword.

Furthermore, I learned file handling, which enables programs to store and retrieve data permanently. I practiced opening, reading, writing, and appending data to files using different file modes. I also learned best practices such as using the "with" statement for automatic file management and combining file operations with exception handling to create safer and more reliable programs.

These lessons provided practical experience in building interactive applications, handling unexpected errors, and managing persistent data, which are critical skills for software development and data analytics.

Concepts Covered

Menu-Driven Programming

- Interactive Menu Systems
- Command-Line Applications (CLI)
- User Choice Handling
- Program Navigation

Program Structure

- "while True" Loops
- "if", "elif", and "else"
- Functions and Modular Programming
- DRY (Don't Repeat Yourself) Principle

Exception Handling

- Syntax Errors
- Runtime Errors (Exceptions)
- Error Management

Exception Handling Blocks

- "try"
- "except"
- "else"
- "finally"

Advanced Exception Handling

- Specific Exceptions
  - "ZeroDivisionError"
  - "ValueError"
  - "FileNotFoundError"
  - "PermissionError"
  - "FileExistsError"
- Custom Exceptions using "raise"
- Exception Hierarchy

File Handling

- "open()" Function
- File Objects
- File Operations

File Modes

- Read Mode ("r")
- Write Mode ("w")
- Append Mode ("a")
- Create Mode ("x")
- Binary Mode ("b")

Reading Files

- "read()"
- "readline()"
- "readlines()"

Writing Files

- "write()"
- Appending Data
- Newline Characters ("\n")

Safe File Handling

- "with" Statement
- Automatic File Closing
- Resource Management

Practical Applications

- Calculator Program
- Banking System Simulation
- Data Storage and Retrieval
- User Input Validation
- Error-Resistant Programs

Key Takeaways

- Learned how to build interactive menu-driven applications using loops, conditions, and functions.
- Improved code organization through modular programming techniques.
- Applied the DRY principle to reduce redundancy and improve maintainability.
- Understood the difference between syntax errors and runtime exceptions.
- Used "try", "except", "else", and "finally" blocks to handle errors gracefully.
- Learned how to catch specific exceptions and create custom exceptions.
- Explored file handling for permanent data storage and retrieval.
- Practiced reading, writing, and appending data to files.
- Used the "with" statement for safe and efficient file management.
- Combined exception handling with file operations to create robust applications.
- Strengthened practical programming skills required for real-world software development and data analytics workflows.
"""


