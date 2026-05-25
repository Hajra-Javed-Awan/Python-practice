#grading system
marks=int(input("enter your marks:"))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="fail"
print("your grade:",grade)

#write the program to check if the nymber is the multiple of 7 or not
num=int(input("enter number:"))
if(num%7==0):
   print("multiple of 7")
else:
   print("not the multiple of 7")

   #NESTED IF ELSE:
   age=int(input("enter the number:"))
   if(age>=18):
       if(age>80):
            print("not drive")
        else:
            print("drive")
    else:
        print("not drive")