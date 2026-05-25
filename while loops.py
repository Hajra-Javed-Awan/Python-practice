#Loops are used to repeat the instructions.
#two main types:
#1.for loop and 2.while loop
#firstlt we discuss about the while loop 
#while condition:
#somework
# n=5
# i=0
# while(i<n):     #wo avriable jin ka through loop lagti ha unay iterators
#     print("hello")
#     i+=1

# print("loop end")

# n=10
# i=0
# while(i<n):     
#     print(i)
#     i+=1

# print("loop end")

#lets some practise questions:
#Q1: Print num from 1 to 100
# n=100
# while(i<=n):
#     print(i)
#     i=i+1
    
# print("loop end")

#Q2: Print num from 100 to 1
# n=1
# i=100
# while(i>=n):
#     print(i)
#     i=i-1
# print("exist")
    
#Q3: WAP to print the multiplication table of a number n.
# n=int(input("enter a number:"))
# i=1
# while(i<=10):
#     print(n, "*", i,"=", i*n)
#     i=i+1

#Q4: WAP to print the element of list:
# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while(i<len(list)):
#     print(list[i])
#     i=i+1


#Q5:WAP to search a number in the tuole using loop:
list=[1,4,9,16,25,36,49,64,81,100]
i=0
x=int(input("enter the number:"))
while(i<len(list)):
    if(list[i]==x):
        print(x,"is found")
        break
    else:
        print(x,"is not found")
        break
    i=i+1