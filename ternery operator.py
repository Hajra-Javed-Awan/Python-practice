#single line if:
light=input("enter light colour:")
nam="stop"if light=="red" else"go"
print(nam)
#0r
light=input("enter light:")
print("stop")if light=="red" else print("go")
#clever if:
age=int(input("plz enter your age:"))
vote=("no you cannot vote","yes you can vote")[age>=18]
print(vote)
