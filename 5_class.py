#IF, IFELSE, ElSE

battery = int(input("Enter battery percentage: "))

if battery > 80:
    print("Battery is highly charged")
elif battery >= 20:
    print("Battery level is normal")
else:
    print("Charge your phone soon")


#nested if else

gender="female"
age=25
gender=input("enter your gender")
if gender=="female":
    print("tickets is free")
else:
    age=int(input("enter your age")) # we have to give int() becouse its numarical space  or number entering section
    if age <5:
        print("free")
    elif age <50:
        print("seniore citizens discount")
    elif age >18:
        print("half tickt")
    else:
        print("pay full ammount ticket")



#whileloop,break and continue,nested whileloop

#whileloop continues to unlimited numbers
b=True # give always true 
i=1
while b: 
    print(f"the number is {i}")
    i=i+1


#whileloop its we can give limitation of numbers
b=True # give always true 
i=1
while b and i <= 10: # i=less than 10 only
    i = i + 1
    print(i)


#using break statment
a=True # give always true 
i=1
while a: 
    print(f"the number is {i}")
    i=i+1
    if i>100: # i=grater than 100 only
      break
print("the end") 


#continue statement

i = 0
while i < 30: # i=less than 30 only
    i += 1
    if i % 2 != 0:
        continue
    print(i)
    


#nested while loop

i = 1

while i <= 3: # i=less than 3 only
    j = 1
    while j <= 3: #j less than 3 only
        print(i, j)
        j += 1  
    i += 1


#one small eg working demo [atm machine]

pin = 8847
trail = 1

while trail < 3:
    input_pin = int(input(f"trials={trail}: "))
    
    if input_pin == pin:
        print("correct")
        break

    trail += 1
else:
    print("incorrect")


"""
What I Learned

In these lessons, I learned how Python uses conditional statements and loops to control the flow of a program. These concepts enable programs to make decisions, execute different actions based on specific conditions, and automate repetitive tasks efficiently.

I explored conditional statements such as "if", "elif", and "else", which allow programs to evaluate conditions and execute appropriate code blocks. I also learned the importance of indentation in Python, as it defines the structure and scope of code blocks. Additionally, I practiced using logical operators ("and", "or", "not") to combine multiple conditions and create more advanced decision-making logic. Through nested conditional statements, I learned how to handle complex scenarios with multiple levels of evaluation.

I also studied "while" loops, which repeatedly execute code as long as a specified condition remains true. I learned how to control loop execution using "break" and "continue" statements and explored nested loops for solving more complex problems. Furthermore, I practiced handling user input within loops to create interactive programs such as authentication systems and input validation processes.

These concepts helped me understand how real-world applications implement decision-making, repetition, and user interaction to create dynamic and intelligent programs.

Concepts Covered

Conditional Statements

- "if" Statement
- "elif" Statement
- "else" Statement
- Nested If-Else Statements
- Decision Making in Programs
- Python Indentation

Logical Operators

- "and"
- "or"
- "not"

Loops

- "while" Loop
- Loop Initialization and Incrementing
- Infinite Loops and Prevention

Loop Control Statements

- "break"
- "continue"

Advanced Topics

- Nested Loops
- User Input in Loops
- Input Validation
- Authentication Logic

Practical Applications

- Even and Odd Number Detection
- Traffic Signal Simulation
- Eligibility Checking Systems
- Discount Calculation Logic
- ATM PIN Verification System

Key Takeaways

- Learned how programs make decisions using conditional statements.
- Understood the role of indentation in defining Python code blocks.
- Applied logical operators to evaluate multiple conditions effectively.
- Built decision-making logic using "if", "elif", and "else" statements.
- Learned how to automate repetitive tasks using "while" loops.
- Used "break" and "continue" to control loop execution.
- Explored nested conditions and nested loops for handling complex scenarios.
- Practiced creating interactive programs using user input and validation techniques.
- Developed problem-solving skills by implementing real-world examples and simulations.
- Strengthened core programming fundamentals that are essential for data analytics, automation, and software development."""