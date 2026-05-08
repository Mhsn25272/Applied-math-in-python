def display_function_logic(n, c):
    """Displays the symbolic representation of the function and its derivative."""
    print(f"\n  f(x)  = 3x^{n} + 12x - {c}")
    print(f"  f'(x) = {3*n}x^{n-1} + 12")


def get_numeric_input(prompt):
    """Handles input and ensures only numeric values are accepted."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️ Error: Please enter a valid number.")


def main():
    print("=" * 45)
    print("   POLYNOMIAL FUNCTION & DERIVATIVE CALCULATOR")
    print("=" * 45)
    print("   General Form: f(x) = 3x^n + 12x - c\n")

    # Step 1: Collect inputs from the user
    x_val = get_numeric_input("  Enter value for x          : ")
    n_pow = get_numeric_input("  Enter exponent (n)         : ")
    c_const = get_numeric_input("  Enter constant value (c)   : ")

    # Step 2: Handle edge cases (Preventing undefined derivatives)
    if x_val == 0 and n_pow < 1:
        print("\n  ⚠️ Warning: Derivative is undefined for x=0 when n < 1.")
        return

    # Step 3: Math Logic (Calculus Implementation)
    # Original function: f(x) = 3x^n + 12x - c
    fx_result = 3 * x_val**n_pow + 12 * x_val - c_const
    
    # Derivative using Power Rule: f'(x) = 3*n*x^(n-1) + 12
    dfx_result = 3 * n_pow * x_val**(n_pow - 1) + 12

    # Step 4: Display Results
    print("\n" + "-" * 45)
    display_function_logic(n_pow, c_const)
    print("-" * 45)
    print(f"  Result f({x_val})  = {fx_result:.2f}")
    print(f"  Result f'({x_val}) = {dfx_result:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()
