cities = ["hubli","pune","bangalore","mumbai","bhuj","patna"]
food = ["pav bhaji","Aloo paratha","kachori","shwarma","manchurian","momos","thupka","pancakes","kebab"]

def print_len(list):
    print(len(list))
    return

# print_len(food)
# print_len(cities)

def print_el(list):
    for item in list:
        print(item, end = " ")
    return

# print_el(food)

def calc_fact(n):
    i = 1
    fact = 1
    # while i <= n:
    #     fact *= i
    #     i += 1
    for i in range(1,n+1):
        fact *= i
    print(fact)   
    return 

#calc_fact(6)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"$ = Rs.",inr_val)
    return

#converter(1)

def odd_or_even(n):
    if(n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    return

#odd_or_even(int(input("Enter a number : ")))        

def calc_sum(n):
    if(n == 0):
        return 0
    else:
        return calc_sum(n-1) + n
    
# result = calc_sum(24)    
# print(result)

def print_list(list , i=0):
    if(i == len(list)):
        return
    print(list[i],end = ",")
    print_list(list,i+1)

print_list(cities) 