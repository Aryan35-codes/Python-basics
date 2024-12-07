#recursive function
def show(n):
    if(n == 0): #base case
        return
    print(n)
    show(n-1)

#show(5)    

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) * n #n! = (n-1)! * n => recurrence relation
    
result = fact(int(input("Enter 'n' : ")))    
print("Factorial = ",result)