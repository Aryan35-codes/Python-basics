# light = "yellow"

# if(light == "red"): #the gap given behind print is called indentation
#     print("Stop")   #as {} is used in some languages 4 spaces are used in python
# elif(light == "yellow"): #elseif -> elif
#     print("Wait")   
# elif(light == "green"):
#     print("Go") 
# else:
#     print("Light is broken")     

#     print("-END OF CODE-")   

# marks = int(input("Enter your marks : "))

# if(marks >= 90):
#     grade = 'A'
# elif(marks < 90 and marks >= 80):
#     grade = 'B'
# elif(marks < 80 and marks >= 70):
#     grade = 'C'    
# else:
#     grade = 'D'  

# print("Grade =",grade)    

age = 13

#nesting
if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("Can drive") 
else:
    print("Cannot drive")          