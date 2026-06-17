'''#output and input
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
print(a*100) # we can give more like 10 500 260 like any number we can give '''

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
