#list intro
#list is the built in function that stores the set of values 
#list is mutable means ka ham list ka element ko access b kr saktay hain or modify b kr saktay hain
#for example:
marks=["80",60,80.89,67,90]
print(marks)
print(type(marks))
print(marks[2])
#LIST SLICING:
num=marks[1:3]
print(num)
#or
print(marks[2:])
#negative slicing:
num1=marks[-6:-2]
print(num1)