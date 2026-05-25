#list.append("sublist")
list=[2,1,5,3]
list.append(4)
print(list)
# not this: print(list.append(4))

#list.sort()         #arrange in assending order
list.sort()
print(list)

#list.sort(reverse=true)    #arrange in dessending order
list.sort(reverse=True)
print(list)

#list.reverse()
list.reverse()
print(list)

#list.insert(idx,element)
list.insert(4,6)
print(list)

#list.pop(idx)
list.pop(4)
print(list)

#list.remove(element)
list.remove(4)
print(list)
