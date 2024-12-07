name = "Aryan" #string
age = 18 #int
price = 500.69 #float  (= -> assignment operator)


# print("My name is : ",name) #ctrl+/ => multi-line comment
# print("My age is : ",age)

# print(type(name)) #type -> gives data types
# print(type(age))  #primary data types:Integers,String,Float,Boolean(True,False),None
# print(type(price))

name1 = 'ar'
name2 = '''ar'''
#print(name1,name2)


old = False
a = None
# print(type(old))
# print(type(a))

a = 2
b = 5
sum = a + b
#print(sum)

#arithmetic operators
x = 5
y = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b) #x to the power y

#relational operators

# print(x == y)
# print(x != y)
# print(x <= y)
# print(x >= y)

#assignment operators(=,+=,-=,/=.*=,%=,**=)
x **= 5 # x = x ** 5
#print(x)

#logical opearators
# print(not False)
# print(not (x > y)) #x = 5,y = 2

val1 = True
val2 = False
# print("AND operator :",val1 and val2)
# print("AND operator :",(x != y) and (x < y))

# print("OR operator :",val1 or val2)
# print("OR operator :",(x != y) or (x < y))

#type conversion
# m = 2
# n = 4.25

# sum = m + n # 2.0 + 4.25 = 6.25
# print(type(sum))
# print(sum)

#type casting
m = int("2")
n = 4.25
o = "3.14"
# print(m + n)
# print(n + float(o))

# A = float("Aryan") #error
# print(type(A))

#inputs

naam = input("Enter your name : ") #always a str
print(type(naam))
print("Welcome", naam)

#To create input of appropriate data type use type casting
umar = int(input("Enter your age :"))
print(type(umar))
print("Your",umar,"years old.") 