#output and input
a="hello"
print(a)

name=input("name : ")
print(name)


#cancatenation
a=input("a : " ) #data
b=input("b : " )  #analyst
c="i want to become a " + a+" "+b  # i want to become data analyst
print(c)

#Another example
b="dr"
d="bro"
e= b +""+ d
print(e)

#formated string 
boy=int(input("boy_age : "))
girl=int(input("girl_age : "))
c= boy-girl
print(f"boy age {boy} girl age {girl} age deffrence is {c}")


# Another example
a=input("enter your job role : ")
print(f"i want to become a {a} ")  


#comment lines

#single line comment 


"""" multi line comment
like this 
a
b
c"""


#repeatations
a=("KANNADIGA . ")
print(a*100) # we can give more like 10 500 260 like any number we can give


#methods 

a="app le"
print(a.upper()) #its convert to caps
print(a.lower()) # its coverts to small
print(a.strip()) # removing unwanted spaces
print(a.replace("apple","b for boll")) # replacing content
 

a=["a","b","e","d","e","f","g","h",]
print(len(a)) # its calculates the total character


#string slicing
name="darshan toogudeepa"
print(name[4]) # 0=d,1=a,2=r,3=s,4=h
print(name[:5]) # darsh
print(name[:6]) #darsha
print(name[-5]) #reverce calculation but its not start with 0 position a p e e d ans is d  
print(name[:])  # full name 
print(name[::2]) # skip 1 postion to another position :
print(name[::1]) #same but its skip 2 position ::


#escape sequence 
print("hello \n world") # its giving next line
print("hello \t world") # its give long tab or space 



''' What I Learned

In these lessons, I learned how to build interactive Python programs by accepting user input and displaying output on the console. I practiced creating simple programs that collect user information, perform calculations, and present results in a clear and readable format.

I also explored Python strings and learned how to manipulate text using various built-in operations and methods. This included combining strings through concatenation, repeating text, modifying strings with methods such as ".upper()", ".lower()", ".strip()", and ".replace()", and formatting output using f-strings. Additionally, I learned how to determine string length, access characters through indexing, extract portions of text using slicing, and format output using escape sequences.

The lessons also introduced the "abs()" function for working with absolute values and demonstrated the importance of comments for documenting code, improving readability, and making programs easier to maintain and understand.

Concepts Covered

- User Input with "input()"
- Output using "print()"
- Interactive Python Programs
- Variables and User Data Handling
- Formatted Strings (f-strings)
- String Manipulation
- String Concatenation and Repetition
- String Methods
  - ".upper()"
  - ".lower()"
  - ".strip()"
  - ".replace()"
- String Length using "len()"
- String Indexing
- String Slicing
- Escape Sequences ("\n", "\t")
- Absolute Value Function "abs()"
- Single-line Comments ("#")
- Multi-line Comments ("''' '''")
- Code Readability and Documentation

Key Takeaways

- Learned how to interact with users through input and output operations.
- Built simple programs that process user-provided data and perform calculations.
- Improved string handling and text-processing skills using built-in Python methods.
- Used f-strings to create cleaner and more readable output.
- Applied indexing and slicing techniques to access and manipulate string data.
- Utilized escape sequences to enhance output formatting.
- Understood the use of the "abs()" function for handling positive values.
- Recognized the importance of writing clear, organized, and well-documented code.
- Strengthened foundational Python skills essential for future data analytics and programming projects.'''