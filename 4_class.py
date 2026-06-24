#TUPLES AND SETS

#tuple : cannot change or modify its order of sequence [indexing]

my =["ka","ap","tn","ts","dl"]
print(my)# getting same output
print(my.append("as")) # its getting error or none becouse can not modify or changes


#sets [unorder and unique collection]

s={1,2,3,4,5,6,7,8,9}
print(type(s)) # its showing set data type

why=set((1,2,3,4,5,6,7)) # its type of set(()) we can also add like this
print(why)

l={8,4,3,7,9,5,"2"}
l.add(5)# we can add or modify in set
l.remove(5) #removing 5 in a set
l.discard(5)# re calling that deleted number or discard 
l.pop()#random delete
print(l)



#set operation [ like matrix]

s1={1,6,8,}
s2={4,3,9,}
print(s1 | s2) #not
print(s1 & s2) #and


#DICTIONARY [its an key:value pair]
gadgets={
    "mobile" : "samsung",
    "laptop" : "dell",
    "tv" : "lg",
    "fridge" :"samsungs",
}
print(gadgets["tv"])#lg
print(gadgets["laptop"])#dell
print(gadgets["mobile"])#samsung
print(gadgets["fridge"])#samsungs
#safe access if getting error do like this 
print(gadgets.get("washing machine","not found"))


#adding and updating in dictionarys
#adding
gadgets["washing machine"] = "godrej",
print(gadgets)

#updating
gadgets["fridge"] = "samsung=2"
print(gadgets)


#methods

"""valus()
keys()
items()
"""

print(gadgets.keys()) #only keys like mobile,laptop,fridge,washing machine
print(gadgets.values()) # their brands



"""
What I Learned

In these lessons, I expanded my understanding of Python data structures by learning about tuples, sets, and dictionaries. These structures provide different ways to organize, store, and manage data efficiently depending on the requirements of a program.

I learned that tuples are ordered and immutable collections, making them suitable for storing data that should remain unchanged throughout program execution. I practiced working with tuple operations such as indexing, slicing, concatenation, and repetition.

I also explored sets, which store unique values and automatically remove duplicates. I learned how sets support mathematical operations such as union, intersection, and difference, making them useful for data comparison and filtering tasks.

Additionally, I studied dictionaries, one of Python's most powerful data structures. Dictionaries store information as key-value pairs, enabling fast and organized data retrieval. I practiced accessing, adding, updating, and removing dictionary elements while exploring commonly used methods such as ".get()", ".keys()", ".values()", and ".items()". I also learned how dictionaries can be used to represent real-world structured data, making them highly valuable for data analysis and application development.

Concepts Covered

Tuples

- Creating Tuples using "()"
- Immutable Data Structures
- Tuple Indexing
- Tuple Slicing
- Concatenation and Repetition

Sets

- Creating Sets using "{}"
- Unique Elements
- Unordered Collections
- Union ("|")
- Intersection ("&")
- Difference ("-")

Dictionaries

- Key-Value Pairs
- Creating Dictionaries using "{}"
- Accessing Values
- ".get()" Method
- Adding and Updating Elements
- Removing Elements with ".pop()"
- Removing Elements with "del"
- ".keys()"
- ".values()"
- ".items()"

Data Structure Comparison

- Lists vs Tuples vs Sets
- Mutability and Immutability
- Ordered vs Unordered Collections
- Handling Duplicate Values
- Indexing and Data Access

Key Takeaways

- Learned how tuples store ordered data that should not be modified.
- Understood the advantages of immutable data structures.
- Used sets to manage unique values and perform mathematical set operations.
- Explored the differences between lists, tuples, and sets.
- Learned how dictionaries organize data using key-value relationships.
- Practiced retrieving, updating, and removing dictionary data efficiently.
- Applied dictionary methods to work with keys, values, and items.
- Understood how structured data can be represented using dictionaries for real-world applications.
- Strengthened foundational Python data structure knowledge that is essential for data analytics, data processing, and software development.
"""