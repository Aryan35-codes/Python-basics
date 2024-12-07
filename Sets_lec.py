collection = {1, 2, 3, 4, "Hare", 2, "Namo!", "Hare"}

# print(type(collection)) #Set is a collection unordered items
# print(collection) #Every element in set must be unique and immutable , thus list and dict are not allowed in set,but sets are mutable
# print(len(collection)) #repeated ekements stored only once

# null_set = set() #empty set syntax
# print(type(null_set))

#set methods 

#collection.add(("Jai jai",108,"Hare")) #adds element in set
# print(collection)

# collection.remove("Hare") #removes elements(even tho multiple) from set,
# print(collection) #shows error if non existing element given


# collection.clear() #empties the set
# print(collection)
# print(len(collection))
 
#print(collection.pop()) #pops random value

set1 = {2, 4, 6, 8}
set2 = {1, 2, 3, 4, 5, 6}

print(set1.union(set2)) #combines both set values and returns new set

print(set2.intersection(set1)) #combines common values and returns new set