#Question 5: 
total_students = ["Student1","Student2","Student3"]

bag_list = [3, 8, 2, 5, 11, 41]

bag_list.sort()
print("the sorted bags list is:",bag_list)

students = [bag_list[i] for i in range(min(len(bag_list), len(total_students)))]

for i, bag in enumerate(students):
    print("Student", i+1, ":",bag)
