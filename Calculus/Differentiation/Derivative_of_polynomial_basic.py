# Simple implementation of the Power Rule

print("function of polynomial fx is: \n 3x^n + 12x - i ")

# input for Polynomial
x = float(input('Enter value for x: '))
n = float(input('Enter exponent n: '))
i = float(input('Enter constant i: '))


# Function Calculation
fx = 3 * x**n + 12 * x - i #fx is function
# Derivative Calculation f'(x)
dfx = 3 * n * x**(n-1) + 12 #dfx is derivative of function

# output value
print(f"f({x}) = {fx}")
print(f"f'({x}) = {dfx}")
