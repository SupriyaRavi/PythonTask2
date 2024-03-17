#Question 3: 

my_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = 0

for num in my_list:
    seen = set()
    original_num = num  # Store the original number
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    if num == 1:
        happy_numbers += 1

print("Total number of happy numbers:",happy_numbers)
