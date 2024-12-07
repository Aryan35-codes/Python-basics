# marks = [94.4, 87.5, 95.2, 66.4, 45.1] #other lang -> Arrays, python -> lists
# print(marks)   # it can store elements of diff types (int,float,string etc)
# print(len(marks))
# print(type(marks))
# print(marks[3])

# student = ["Arjun",92.3,18,"Gurgaon"]
# print(student)                       
# print(len(student[3]))
# print(type(student))
# student[3] = "Haryana"    #strings -> immutable
# print(student[3])         #lists -> mutable
# print(student[2:4])       #lists slicing
# print(student[-4:-2])     #negative indexing

#list methods
list = [2, 1, 3]
list.append(4) #adds one element(int,float,char) at the end
print(list)
list.sort() #sorts in ascending order
print(list)
print(list.append(9))
list.sort(reverse = True) #sorts in decending order
print(list)
list.reverse() #reverses list
print(list)
list.insert(4,66) #insert element at index (index,element)
print(list) 
list.remove(66) #removes first occurence of given element
print(list)
list.pop(4) #removes element at given index
print(list)