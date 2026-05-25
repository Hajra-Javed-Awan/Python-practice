#SET
#set is the collection of unordered items
#each element in the set is immutable
# ignore duplicate values 
#example:
# collection={1,4,3,"hajra",2,1}
# print(collection)
# print(type(collection))
# print(len(collection))

#METHODS:

#1:set.add(ele)
#its purpose is to add element into the set....
collection= set()
collection.add(4)
collection.add(56.90)
collection.add("awan")
collection.add("hjara")
collection.add("javed")
collection.add(4)
print(collection)

#2:set.remove(element)
#its purpose it to remove the specific element... 
collection={1,"awan",3,"hajra",2,"javed",1}
collection.remove("hajra")
print(collection)

#3:set.clear()
#its purpose is to clear all the vlues from set...
# collection.clear()
# print(collection)

#4:set.pop()
#its purpose is to pop out the random the values...
# collection.pop()
print(collection.pop())

#THE MOST IMPORTANT METHODS........
#set1.union(set2)
#taking the union of both sets(means dono sets ka elements likh dain gAY)
set1={6,3,9,6,3,6,2,1}
set2={4,5,8,7,9,0,10}
print(set1.union(set2))

#set1.intersection(set2)
#taking the common values of both sets...
print(set1.intersection(set2))

