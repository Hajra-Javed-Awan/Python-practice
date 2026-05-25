#break:
#it is used to terminate the loop
# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# x=int(input("enter the number:"))
# while(i<len(list)):
#     if(list[i]==x):
#         print(x,"is found")
#         break
#     else:
#         print(x,"is not found")
        
#     i=i+1

# continue:
#it is used to terminate the execution of current loop / CURRENT EXECUTION TERMINATE
# n=5
# i=1
# while(i<=n):
#     if(i==3):
#         i=i+1
#         continue
#     print(i)
#     i=i+1    

#EXAMPLE:
#PRINT ONLY ODD NUM FROM 1 TO 10:
# n=10
# i=1
# while(i<=n):
#     if(i%2==0):
#         i=i+1
#         continue
#     print(i)
#     i=i+1

#PRINT ONLY even NUM FROM 1 TO 10:
n=10
i=1
while(i<=n):
    if(i%2!=0):
        i=i+1
        continue
    print(i,"is even num")
    i=i+1