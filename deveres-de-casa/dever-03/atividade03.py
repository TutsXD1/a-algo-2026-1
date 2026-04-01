def is_palindrome(array):
    """
    Checks if an array is a palindrome using recursion.
    
    Args:
        array (list): The list of elements to check.
        
    Returns:
        bool: True if the array is a palindrome, False otherwise.
    """
    # Base case: an empty array or an array with one element is a palindrome
    if len(array) <= 1:
        return True

    # Check if the first and last elements are equal
    if array[0] == array[-1]:
        # Recursive call with the inner part of the array
        return is_palindrome(array[1:-1])

    return False


def main():
    """Main function to test the palindrome logic."""
    array1 = [0, 1, 2, 3, 2, 1, 0]
    array2 = ["a", "b", "b", "a"]
    array3 = ["a", "b", "c", "b", "a"]
    array4 = ["a", "b", "c", "f", "b", "a"]

    test_cases = [array1, array2, array3, array4]

    for i, arr in enumerate(test_cases, 1):
        result = is_palindrome(arr)
        status = "Is a palindrome" if result else "Is NOT a palindrome"
        print(f"array{i} = {arr} -> {status}")


if __name__ == "__main__":
    main()