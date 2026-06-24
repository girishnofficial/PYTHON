#Assignment operators

x=5
x-=3 #8
x/=2 #6
x*=4 #24
x+=6 #11
print(x) #10.5


#Comparision operators

a=20
b=5
print(a==b) # 20 and 5 is not same
print(a!=b) # 20 and 5 is not equel so yes 
print(a>b)  # a is greater than b
print(a<b)  # a is less than b
print(a<5)  # a is less than 5
print(b>20) # b is greater  than 20



#logical operators[AND,OR,NOT] 

a= True
b= False
print(a and b) #both are true
print(a or b) #at least one is true
print(not a) #reverse if true is a false and false is a true
#and we can also use symobol of these  eg:   &&(and)  ||(or)   not (!)



#membership operators

my_list=["a","b","c","d","e","f","g",]
my_string=("python")
print(a in my_list) #my list have a
print("z" not in my_string) # my string not have z
print("p" in my_list) #my list not have p
print("n" in my_string) #my string has n
print("f" in my_string) #my string not have f


#bitwize operators(binary numbers)
a=5
b=3
print(a&b) # and
print(a^b) #or
print(a|b) #xor
print(a>>b) #right shift
print(a<<b) #left shift


#list

fruits=["apple","bannan","cherry","grapes","orange","guava",]
print(fruits)

#deleting items:
print(fruits.pop()) # its deleting last item of fruites eg:guava
print(fruits.pop(2))# we can give index position eg: 0>apple ,1>bannana, 2>cherry ans is cherry 

#adding items:
fruits.append("water_melon") # adding the items
print(fruits)
fruits.insert(4,"rose")# we can add which place we can add in row eg : rose was 5th position becouse index start with 0
print(fruits)

#removing
fruits.remove("orange")
print(fruits)


#slicing list
#syntax:- list_name[sart:stop:step]  (inclusive,exclusive,defualt)

numbers=[0,1,2,3,4,5,6,7,8,9]
print(numbers[:4]) #[0, 1, 2, 3]
print(numbers[::4]) #[0, 4, 8]
print(numbers[:7]) #[0, 1, 2, 3, 4, 5]
print(numbers[::2]) #[0, 2, 4, 6, 8]
print(numbers[::2]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2]) #[0, 1, 2, 3, 4, 5]
print(numbers[:]) #0123456789
print(sum(numbers)) # total
print(len(numbers)) # lenght of characters
z=["4","g","7","a","8","z",]#why becoues iam already taken ordering charecter 12345678 so thats whay write this 
print(sorted(z))
print(len(z))




""" 
What I Learned

In these lessons, I gained a deeper understanding of Python data structures and operators, which are essential for writing efficient and logical programs. I learned how to create and work with lists, one of Python's most versatile data structures for storing and managing collections of data.

I explored list indexing, including negative indexing, and practiced accessing, modifying, and organizing data using various built-in list methods. I also learned how to extract portions of a list using slicing techniques and worked with nested lists to represent multi-dimensional data structures such as matrices.

Additionally, I was introduced to the "NoneType" data type, which represents the absence of a value. I learned how different categories of operators are used to perform calculations, assign values, compare data, evaluate logical conditions, check membership within sequences, and perform binary-level operations. These concepts strengthen problem-solving abilities and form a strong foundation for future programming and data analysis tasks.

Concepts Covered

Lists

- Creating Lists using "[]"
- List Indexing
- Negative Indexing
- List Slicing
- List Modification
- Nested Lists and Matrices

List Methods and Functions

- "append()"
- "pop()"
- "remove()"
- "insert()"
- "len()"
- "sorted()"
- "sum()"
- "count()"
- "index()"
- "reverse()"

Data Types

- "NoneType"

Operators

- Assignment Operators ("=", "+=", "-=", "*=")
- Comparison Operators ("==", "!=", ">", "<", ">=", "<=")
- Logical Operators ("and", "or", "not")
- Membership Operators ("in", "not in")
- Bitwise Operators ("&", "|", "^")

Key Takeaways

- Learned how to store, access, and manipulate collections of data using lists.
- Understood indexing and slicing techniques for efficient data retrieval.
- Applied common list methods to add, remove, search, sort, and organize data.
- Explored nested lists for representing multi-dimensional data structures.
- Understood the purpose of the "NoneType" data type.
- Learned how assignment operators simplify variable updates.
- Used comparison and logical operators to evaluate conditions and make decisions.
- Applied membership operators to check the presence of elements in sequences.
- Gained introductory knowledge of bitwise operations and binary-level processing.
- Strengthened core Python skills that are important for data analytics, problem-solving, and software development.
"""