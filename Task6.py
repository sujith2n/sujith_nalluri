import math

# Step 1: Ask the user for a number
num = float(input("Enter a positive number: "))

# Step 2: Perform calculations
if num > 0:
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)       # Natural logarithm (base e)
    sine_val = math.sin(num)      # Sine in radians

    # Step 3: Display the results
    print("\nResults:")
    print(f"Square root of {num} = {sqrt_val}")
    print(f"Natural logarithm of {num} = {log_val}")
    print(f"Sine of {num} radians = {sine_val}")
else:
    print("Error: Please enter a number greater than 0 for valid sqrt and log computations.")
