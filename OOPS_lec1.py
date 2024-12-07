# #Class is a blueprint for creating objects

#creating class (blueprint)
# class Student:
#     name = "Karan Johar"

# #creating object(instance)
# s1 = Student()
# print(s1.name)  
# print(s1)

#s2 = Student()
#print(s2.name)  

# class Car:
#     color = "blue"
#     brand = "TATA"
#     price = 6.5

# car1 = Car()
# print(car1.color)
# print(car1.price)

# class Student:
#     #self is a parameter of reference to current instance of class,and is used to access variables that belongs to the class 
#     #default constructor
#     def __init__(self): 
#         pass
    
#     college_name = "D.Y Patil"#class attribute

#     #parameterized constructor
#     def __init__(self, name, marks): #constructor(init => initialization)
#        #print(self) #self directs towards objects(s1) #name is an arguement constructor takes
#         self.name = name #object attribute > class attribute
#         self.marks = marks
#         # print("adding new student in Database..")

    #   @staticmethod #decorator
    #   def hello(): 
    #   print("hello")

#     def welcome(self): #class methods 
#         print("welcome student",self.name)  

#     def get_marks(self):
#         return self.marks

# s1 = Student("karan",96)# () <- for calling constructor or __init__ function    
# #print(s1.name, s1.marks)   #name is called an attribute 
# s1.welcome()
# print(s1.get_marks())

# # s2 = Student("arjun",89)
# # print(s2.name, s2.marks)

# # print(Student.college_name) #or s2.college_name

class Car:                #4 pillars of OOPs : Abstarction, Encapsulation, Inheritance, Polymorphism
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self): #Encapsulation -> Wrapping data and functions into  a single unit(object)
        self.clutch = True
        self.acc = True
        self.brk = False
        print("car started..")

car1 = Car()
car1.start() #Abstraction -> Hiding the implementation of a class and only showing the essential features to the user        