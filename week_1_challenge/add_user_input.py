# creating an empty list
numbers = []

# ask the user how many numbers they want to enter
while True:
    try:
        num = int(input("How many numbers do you want to enter? "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# loop through the range of the number of numbers the user wants to enter
for i in range(num):
    # ask the user to enter a number
    while True:
        try:
            number = int(input(f"Enter number {i+1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    # add the number to the list
    numbers.append(number)
    # print the list
    print(f"You have added {number} to the list. The list now looks like this: {numbers}")

# calculate the sum of the numbers in the list
total_sum = sum(numbers)
print(f'The sum of the numbers in the list is: {total_sum}')
