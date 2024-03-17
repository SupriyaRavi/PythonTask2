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


#Question 4:
num = int(input("Enter an integer: ")) 

num_str = str(num) 

first_digit = num_str[0]  
last_digit = num_str[-1]  

print("First digit:", first_digit)
print("Last digit:", last_digit)


#Question 5: 
total_students = ["Student1","Student2","Student3"]

bag_list = [3, 8, 2, 5, 11, 41]

bag_list.sort()
print("the sorted bags list is:",bag_list)

students = [bag_list[i] for i in range(min(len(bag_list), len(total_students)))]

for i, bag in enumerate(students):
    print("Student", i+1, ":",bag)



#Question 6:

l1 = [2,8,5,7,3]
l2 = [4,5,3,1,8]
l3 = [5,8,9,1,0]


duplicates = set(l1) & set(l2) & set(l3)

print("Duplicates:", duplicates)

