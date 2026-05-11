def display_function_logic(x_val,f_coef,g_coef,n_pow_f,n_pow_g):
    """Displays the symbolic representation of the function and its derivative."""
    print(f"Formula of product rule form is: \n f'(x) * g'(x) = f'(x) * g(x) + f(x) * g'(x)")
    print(f"\n  f(x) * g(x)  = [{f_coef}X^{n_pow_f}) * ({g_coef}X^{n_pow_g}]")
    print(f"  f'(x) * g'(x) = {n_pow_f} * {f_coef} * X^({n_pow_f} - 1) * g(x) + f(x) * {n_pow_g} * {g_coef} * X^({n_pow_g} - 1)")


def get_numeric_input(prompt):
    """Handles input and ensures only numeric values are accepted."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️ Error: Please enter a valid number.")


def main():
    print("=" * 45)
    print("   PRODUCT RULE & DERIVATIVE CALCULATOR")
    print("=" * 45)
    print(f"   General Form: \n f'(x) * g'(x) = f'(x) * g(x) + f(x) * g'(x)")

    # Step 1: Collect inputs from the user
    x_val  = get_numeric_input("  Enter value for x          : ")
    f_coef = get_numeric_input("Enter coefisien of f function: ")
    g_coef = get_numeric_input("Enter coefisien of g function: ")
    n_pow_f = get_numeric_input("  Enter exponent of f: ")
    n_pow_g = get_numeric_input("  Enter exponent of g: ")

    # Step 2: Handle edge cases (Preventing undefined derivatives)
    if x_val == 0 and (n_pow_f < 1 or n_pow_g < 1) :
        print("\n  ⚠️ Warning: Derivative is undefined for x=0 when n < 1.")
        return

    # Step 3: Math Logic (Calculus Implementation)
    # Original function: f(x) = 3x^n + 12x - c
    f_result = f_coef * x_val ** n_pow_f
    g_result = g_coef * x_val ** n_pow_g
    function_result = f_result * g_result 
    
    # Derivative using Product Rule
    f_prime = n_pow_f * f_coef * (x_val ** (n_pow_f - 1)) 
    g_prime = n_pow_g * g_coef * (x_val ** (n_pow_g - 1))
    dfx_result = f_prime * g_result + f_result * g_prime
  
    # Step 4: Display Results
    print("\n" + "-" * 45)
    display_function_logic(x_val,f_coef,g_coef,n_pow_f,n_pow_g)
    print("-" * 45)
    print(f"  Result of f({x_val}) * g({x_val})  = {function_result:.2f}")
    print(f"  Result f'({x_val}) * g'({x_val}) = {dfx_result:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()
