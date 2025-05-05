# Step 1: Define the factorial function using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Step 2 & 3: Call the function with a sample number and print the result
sample_number = int(input("Enter a Number : "))
result = factorial(sample_number)
print(f"The factorial of {sample_number} is {result}.")
