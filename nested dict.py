# NESTED DICTIONARY
# is ma ham dict la andr hi kisi key ki further dict bna daity hain
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
print(student)
print(student["subject"])
# print(student["subject"]["networking"])
nmae=student["subject"]["networking"]
print(nmae)