# info = {
#     "keys" : "values",
#     "name" : "Aryan",
#     "learnings" : ["C","Java","python"],
#     "topics" : ("dictionary","sets","tuples"),
#     "age" : 18,
#     "is_adult" : True,
#     "marks" : 93.7,
#     5 : 1
# } #Keys and values can be any form of data(int,float,boolean,string,list)
#   #only tuple cannot be a key cuz dictionary is mutable and tuple isn't
#   #They are unordered and don't allow duplicate keys

# print(type(info)) 
# info["surname"] = "Revankar" #new key and value assigned
# print(info)

# print(info["topics"])
# print(info[5])

# info["name"] = "Jeevita" #in dictionary full list can be changed not single element of them
# print(info["name"]) #new value assigned

student = {
    "name" : "Tushar Shetty",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
#nested dictionary

#dictionary methods

#print(student["subjects"]["math"])
# print(list(student.keys())) # or print(student.keys())#returns all keys #dict typecasted to list can also be typecasted to tuple 
# print(len(student)) #  or print(len(list(student.keys())))

# print(student.values()) # or print(list(student.values())) #returns all values

# print(student.items()) #returns (key , value) pairs
# pairs = list(student.items())
# print(pairs[1])

#.get -> gives value of specified key
print(student["name"]) #if key is wrong ,gives error
print(student.get("name")) #if key is wrong , gives no error gives NONE
#While coding in practical , if error comes its difficult to find them
#thus using this function helps as code runs forward and doesn't
#stop showing error

#student.update({"city" : "Ahmedabad"})
new_dict = {"city" : "Ahmedabad","skills" : "Dance"}
student.update(new_dict) #inserts items in dict
print(student)

null_dict = {} #we can also make an empty dict,in which we can add elements later
print(type(null_dict))