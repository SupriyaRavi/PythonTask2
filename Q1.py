#Question 1
my_list = [10, 501, 22, 37, 100, 999, 87, 351]

even_num = []
odd_num = []

for num in my_list:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

print("Even numbers:", even_num)
print("Odd numbers:", odd_num)
