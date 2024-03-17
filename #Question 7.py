#Question 7

my_list= [1, 2, 3, 2, 1, 4, 5, 4, 6]

# Iterate through each element in the list
for i in my_list:
    # Check if the current element appears only once in the list
    if my_list.count(i) == 1:
        # If yes, it's the first non-repeating element
        print("First non-repeating element:", i)
        break  