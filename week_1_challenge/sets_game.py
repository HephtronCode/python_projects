# Get input for the first set
input1 = input("Enter integers for the first set, separated by spaces: ")
set1 = set(map(int, input1.split()))

# Get input for the second set
input2 = input("Enter integers for the second set, separated by spaces: ")
set2 = set(map(int, input2.split()))

# Find common elements
common_elements = set1.intersection(set2)

# Print the common elements
print("The common elements in both sets are:", common_elements)