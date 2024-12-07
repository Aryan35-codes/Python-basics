# tup = (2, 1, 3, 1) #tuple is immutable
# print(type(tup))
# print(tup[2])
# tup1 = ()
# print(tup1)
# tup2 = (1) #python will think 1 as an integer
# print(type(tup2))
# tup3 = (1,) #python will think 1 as a tuple data
# tup4 = ("Ni hao")
# print(type(tup4))
# print(tup[0:2])

#Tuple methods

tup = (2, 1, 3, 1)
print(tup.index(3)) #returns index of first occurence element
print(tup.count(2)) #counts total occurence