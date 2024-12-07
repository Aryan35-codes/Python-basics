# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Sanju")
# print(s1.name)
# del s1 #del(delete) keyword ,deletes object and obj.attribute
# print(s1.name)        

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #__ means making class attribute pvt , it can be used only within class

#     def   reset_pass(self):
#         self.__acc_pass = "0000"
#         print(self.__acc_pass)

# acc1 = Account(1234567890, 7319)

# print(acc1.acc_no,acc1.acc_pass) 
# acc1.reset_pass()

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello man!")

#     def welcome(self):
#         self.__hello()    

# p1 = Person()

# #print(p1.__name)
# #print(p1.__hello()) 

# p1.welcome()

# class Car: #parent class
#     #color = "blue"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop(): 
#         print("car stopped.") 

# class ToyotaCar(Car): #child class #inheritance=>When one class(child/derived) derives the properties and methods of another class(parent/base)
#     def __init__(self, brand): #single inheritance
#         self.brand = brand

# # car1 = ToyotaCar("fortuner")
# # car2 = ToyotaCar("prius")     
 
# # print(car1.name)  #3 types -> Single , Multi-level , Multiple inheritance
# # print(car2.stop())
# # print(car1.color)

# class Fortuner(ToyotaCar): #multilevel inheritance
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()        

# class A: #multiple inheritance
#     var1 = "Hi welcome"

# class B:
#     var2 = "Namaste welcome"

# class C(A, B):
#     var3 = "Vanakamm welcome"        

# div = C()
# print(div.var2)

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")  

class Toyotacar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type) #super() method is used to access methods of parent class
                
car1 = Toyotacar("prius","diesel")
print(car1.type)

