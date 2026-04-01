import sys


def function_r(n):
    """Calculates F(n) using recursion."""
    if n == 1:
        return 1
    
    return 2 * function_r(n - 1) + n**2


def function_closed(n):
    """
    The closed form of the function is given by:
    F(n) = 13 * 2^(n - 1) - n^2 - 4n - 6
    """
    return 13 * (2 ** (n - 1)) - n**2 - 4 * n - 6


def main():
    """Main execution block."""
    sys.setrecursionlimit(2000)
    
    try:
        n_str = input("Enter an integer value for n (n >= 1): ")
        n = int(n_str)
    
        if n < 1:
            print("Base case is F(1), so enter a value >= 1.")
            return
    
        # Calculating using both methods
        recursive_result = function_r(n)
        closed_result = function_closed(n)
    
        print("\n--- Results ---")
        print(f"Using recursion: F({n}) = {recursive_result}")
        print(f"Using closed formula: F({n}) = {closed_result}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()