# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name,"your avg score is", sum/3)    


# s1 = Student("Jeevita", [99, 98, 97])   
# s1.get_avg()     

# s1.name = "Aryan"
# s1.get_avg()
        
class Account:
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self, amount):
        self.bal -= amount
        print("Rs.",amount," was debited") 
        print("Total balnace = ",self.get_balance())

    def credit(self, amount):
        self.bal += amount
        print("Rs.",amount," was credited")   
        print("Total balnace = ",self.get_balance()) 

    def get_balance(self):
        return self.bal    

acc1 = Account(11000, 1234567890)
print("Balance = ",acc1.bal)
print("Account no = ",acc1.acc_no)

acc1.debit(5000)
acc1.credit(20000)
print("Balance = ",acc1.get_balance())