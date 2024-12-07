# str1 = " This is Aryan's code.\n It's created in python " #escape sequence character 
# str2 = " This is Aryan's code.\t It's created in python " #\n -> nextline , \t -> tab
# str1 = "Aryan"
# str2 = "Revankar"

# print(str1 +" "+ str2) #concatenation
# print(len(str1)) #length of string

# print(str1[4]) #indexing

# print(str2[2:5]) #slicing -> accesing parts of a string #ending index is not included
# print(str1[3:]) # <= means str1[3:len(str1)] 
# print(str1[:3]) # <= means str1[0:3]

# strex = "Apple" #negative indexing is only for slicing
# print(strex[-5:-2]) #in python negative index is allowed,here it goes backwards A->-5,e->-1 


str = "i am studying python from Youtube"
print(str.endswith("ube")) #returns True if str ends with 'ube'
print(str.capitalize()) #capitalizes 1st character
print(str.replace("t","do")) #str.replace(old,new) #replaces all occurence of old
print(str.find("from")) #gives index of first occurence of char
print(str.count("o"))
