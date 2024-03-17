#Question 2 

my_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []

for num in my_list:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:                
                break
        else:
            prime_numbers.append(num) 

print("List of prime numbers:", prime_numbers)
print("Total prime numbers:", len(prime_numbers))