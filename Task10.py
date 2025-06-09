# Step 1: Create list of numbers from 1 to 10
num = list(range(1, 11))  # [1, 2, 3, ..., 10]

# Step 2: Extract the first 5 elements using slicing
first_five = num[0:5]  # [1, 2, 3, 4, 5]

# Step 3: Reverse the extracted list using slicing
reversed_five = first_five[::-1]  # [5, 4, 3, 2, 1]

# Step 4: Print all the lists
print("Original list:", num)
print("Extracted first five elements:", first_five)
print("Reversed extracted list:", reversed_five)
