#forloops

for i in range(1,20):#its a telling to give number range of 1 to 20
    print(i)


#range() function
for i in range(1,50,4): # its start,stop,step process its means we want 1 to 50 number but its leave 4 4 digit of 1 to 50
    print(i,end=" ")


#eg for charactors
name="data analyst"
for role in name:# we have to give variable name like eg :role etc 
    print(role)
    print(role*8)# can give reapetation how much we want like 8 or 5 ,56,745 etc


#enumerate function() finding the index position or place 
e= (56,75,78,76,65,64,54,43,43,2,76,32,39,23,)
for index,num in enumerate(e): #its give the instruction of index position
    print(f"{num} is an {index}th index")  #76 is an 0th index   and  75 is an 1th index  etc


#using else in forloop
f=(6,8,4,7,4,7,8,8,5,4,6,77,8,85,88)
for go in f:#giving variable
    print(go)
    if go <1: # its giving grater value more than 1
        print("  ") # giving blank space for visual looking
        break #waiting the all numbers are enters or not
else: #its giving out of block becouase all the number enters than only show next condition
        print("yess all printed") #final 


#nested forloop (tables)
for i in range(1,100):
     for j in range (1 ,10):
          print(f"{i} X = {j} = {i*j}")


#looping in advance

#total sum
r=(2,4,5,6,7,8,9,9,8,9,9,4,6,7,8,8,)
total=0 #its giving for calculation variable like 0 is an number no value for this number 
for red in r:
     print(total)
     total=total+red       #calculate like 2+4=6+4=10 like this 
     print(total)


#dubling loops
d=[2,9,2,3,4,7,2,4,89,2,58,8,22,45,58,2,2,58,5,52,2,4,4,7]
dl=[]
for num in d:
 dl.append(num*2)
 print(dl)

 #output like this 
"""[4]
[4, 18]
[4, 18, 4]
[4, 18, 4, 6]
[4, 18, 4, 6, 8]
[4, 18, 4, 6, 8, 14]
[4, 18, 4, 6, 8, 14, 4]
[4, 18, 4, 6, 8, 14, 4, 8]
[4, 18, 4, 6, 8, 14, 4, 8, 178]
[4, 18, 4, 6, 8, 14, 4, 8, 178, 4]
[4, 18, 4, 6, 8, 14, 4, 8, 178, 4, 116] etc """


#range in loop
student=("mr","bro","dr","dboss","power","rockey")
marks=("34","43","56","78","59","48",)
stu_marks={} # calculation space
for i in range(len(student)):#assign the valus for each pesrson  range(index)  and lenght of the student
    stu_marks[student[i]]=marks[i] #adding the values for each person
    print(stu_marks) 
    print("\n")#next line



#dictionarys in forloop
ab={"g":100,"i":170,"r":600,"i":120,"s":140,"h":173,"N":850} # wecan use single rowise
for cd in ab.items(): #item means key value pair
  print(cd)
  print("\n")#next line


#list comprehension: list have this symbole[]
#syntax : exp for item in collection 
c=[4,7,5,2,9]
dl=[item*2 for item in c] #its double the nuber eg 4+4 =8  and 7+7=14 etc
print(dl)


#dictionary list comprehesion and letter lenght

temp={
    "beng" : 85,
    "myso" : 50,
    "mandya" : 45,
    "gulbar" :89,
    "raichur": 79,
}
temp={key:value for key,value in temp.items() if value > 10} #key valus getting below 10 
print(temp)


#splitting

s="this is python program"
l=s.split() # splitting part part wize ans is ['this', 'is', 'python', 'program']
print(l)


#list input And split()
print("hello everybody") 
x=input("enter a list:  ").split()
t=(num for num in x) 
print(x)


"""

What I Learned

In these lessons, I deepened my understanding of Python loops and learned how to write more efficient and readable code using comprehensions. I explored "for" loops, which are commonly used to iterate through collections such as lists, tuples, strings, and dictionaries. Unlike "while" loops, "for" loops are particularly useful when the number of iterations is known or when working with sequences of data.

I learned how to use the "range()" function to generate numeric sequences and the "enumerate()" function to access both the index and value of items during iteration. I also practiced controlling loop execution using "break" and "continue" statements and understood how the "else" block can be used with loops.

Additionally, I explored nested loops and applied them to practical examples such as generating multiplication tables. The lessons also introduced list comprehensions and dictionary comprehensions, which provide a concise and Pythonic way to create and manipulate data structures. Finally, I learned how to handle multiple user inputs efficiently using the ".split()" method combined with type conversion techniques.

These concepts improved my ability to process data efficiently and write cleaner, more optimized Python code.

Concepts Covered

For Loops

- "for" Loop Basics
- Iterating Through Lists, Tuples, Strings, and Dictionaries
- Dictionary Iteration using ".items()"

Loop Functions

- "range(start, stop, step)"
- "enumerate()"

Loop Control Statements

- "break"
- "continue"
- "else" with Loops

Nested Loops

- Nested "for" Loops
- Multiplication Table Generation

Comprehensions

- List Comprehension
- Dictionary Comprehension
- Conditional Comprehensions

String Handling and Input

- ".split()" Method
- Multiple User Inputs
- Type Conversion
- Data Processing with Lists

Key Takeaways

- Learned how to use "for" loops to iterate through various data structures.
- Understood the differences between "for" loops and "while" loops.
- Applied the "range()" function to generate custom sequences of numbers.
- Used "enumerate()" to access item positions and values simultaneously.
- Controlled loop execution using "break", "continue", and "else".
- Explored nested loops to solve multi-level programming problems.
- Learned how list comprehensions simplify code and improve readability.
- Created dictionaries efficiently using dictionary comprehensions.
- Processed multiple user inputs using ".split()" and type conversion.
- Developed more Pythonic coding practices for handling data efficiently.
- Strengthened foundational skills that are highly relevant for data analytics, data processing, and automation tasks.
"""