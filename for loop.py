#for loop:
#it is used for traversing list,tuple,and strings.
#for element in list
#somework
#traversing of list:
list=[3,5,1,8]
for value in list:
    print(value)

vaggies=["lady finger","bringle","cucumber","capsicum","potato","tomato"]
for value in vaggies:
    print("vaggies are:",value)

#for loop with else:
list=[3,5,1,8]
for value in list:
    print(value)
else:
    print("end")

#traversing of string:
name="hajra javed awan"
for value in name:
    print("name:",value)

#lets practise some questions:
#Q1: print the element of following list:
list=[1,4,9,16,25,36,49,64,81,100]
for value in list:
    print("single value:",value)

#Q2:search the number x from tuple using list:
list=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number:"))
i=0
for value in list:
    if(value==x):
        print("value found:",x)
        i=i+1
else:
    print("value not found")