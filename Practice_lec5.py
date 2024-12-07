#while loop
# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# n = int(input("Enter 'n' : "))
# i = 1
# while i <= 10:
#     print(n," * ",i," = ",n * i)
#     i += 1

#nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#traverse(travelling from element to element)
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# nums = []
# i = 1
# while i <= 10:
#     square = i * i
#     nums.append(square)
#     i += 1

# print(nums) 

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# idx = 0 #initialization
# x = 25
# while idx < len(nums): #condition
#     if(nums[idx] == x):
#         print("'x' Found at index : ",idx)
#         break #terminates loop when encountered
#     else:
#         print("finding....")    
#     idx += 1 #updation
#this method of searching is called linear searching

#//#
# i = 0
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue #terminates execution in current iteration and continues iterartion in next loop
#     print(i)
#     i += 1

# print("END")

#for loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for el in nums:
#     print(el)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25)
# x = 25

# idx = 0
# for el in nums:
#     if(el == x):
#         print(x,"found at idx : ",idx)
#     idx += 1    

#range()
# for i in range(101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n = int(input("Enter a number : "))
# for i in range(0,11):
#     print(n," * ",i," = ",n * i)

# n = int(input("Enter 'n' : ")) #sum of 'n' numbers
# sum = 0 
# i = 0
# # for i in range(n+1):
# #     sum += i

# while i <= n:
#     sum += i
#     i += 1

# print("Total sum = ",sum)    
    
n = int(input("Enter 'n' : "))
fact = 1
i = 1
for i in range(1,n+1):
    fact *= i

print("Factorial of ",n," is ",fact)    