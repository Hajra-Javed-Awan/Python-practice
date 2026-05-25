# DICTIONARY:
# dict are used to store adta values in key value pairs
# student={
#     "name":"Hajra",
#     "father name":"Muhammad Javed Awan",
#     "roll no:":13,
#     "dept":"CS",
#     "section":"A",
#     "semester":5,
# }
# print(student)
# print(type(student))
# print(student["name"])
# student["name"]="hajra awan"
# print(student)
# student["session"]=2032
# print(student)
#ham string,int,float,tuple,boolean lo as a key use kr sktay hainbut we cannot use the list as a key bcz list ca be mutable

#METHODS OD DICT:
#1.dict.key()
#it is used to returns all the keys 
#it cannot return the key of nested dict
student={
    "name":"hajra javed awan",
    "roll no:":13,
    "session":"2023-2027",
    "semester":4,
    "subject":{
        "networking":82,
        "assembly":70,
        "arabic":68,
        "english":80,
        "financial":68,
        "automata":72,
    }
}
print(student.keys())

#2:len(dict)
#it calculate the total length of dict
print(len(student))

#3:dict.values()
#it return all the values include nested
print(student.values())

 #4:dict.items()
 #it returns all the key value pairs
#  print(student.items())
#agr ham sirf print function use krtay hain is dunction ko execute krnay ka lia the  ya output ma error show karay ga
print(list(student.items()))
#if we have to access key value pair indiviualy then we do this:
# class=list(student.items())
# print(class[0]) 

#5:dict.get("key")        #we have to directly use this function in print state..
print(student.get("session"))