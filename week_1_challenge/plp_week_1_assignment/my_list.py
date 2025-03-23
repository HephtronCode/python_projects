my_list = []

my_list.append(10, 20, 30, 40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.remove(70)

# Sort the list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list.
print(my_list.index(30))