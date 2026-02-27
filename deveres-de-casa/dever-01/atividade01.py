import random
import time

def insertion_sort(array):
    """
    Insertion Sort Algorithm.
    It works by comparing all elements with all previous ones. 
    Best case: O(n)
    Worst case: O(n^2)
    """
    n = len(array)

    # A list with 1 or fewer elements is already sorted
    if n <= 1: 
        return array
        
    # Doesn't start at 0; the first element is already considered sorted
    for i in range(1, n): 
        key = array[i]  # Element being analyzed (key)
        j = i - 1
        
        # Move elements of array[0..i-1] that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j] 
            j -= 1
            
        array[j + 1] = key

    return array


# --- Tests ---
if __name__ == "__main__":
    sizes = [10, 25, 50, 100, 250, 500, 1000, 5000, 10000, 20000]

    print("Starting tests...\n")

    for size in sizes:
        # Generate a list of random integers
        original_array = [random.randint(1, 100000) for _ in range(size)]

        # Creating copies to ensure fair comparison
        array_for_insertion = original_array.copy()
        array_for_sorted = original_array.copy()

        # Measuring Insertion Sort
        start_time_insertion = time.time()
        insertion_sort(array_for_insertion)
        end_time_insertion = time.time()
        time_insertion = end_time_insertion - start_time_insertion

        # Measuring native sorted()
        start_time_sorted = time.time()
        sorted(array_for_sorted)
        end_time_sorted = time.time()
        time_sorted = end_time_sorted - start_time_sorted

        # Printing results with formatted floating point numbers 
        print(f"List size: {size}")
        print(f"Insertion Sort execution time: {time_insertion:.6f} seconds")
        print(f"sorted() execution time:       {time_sorted:.6f} seconds")
        
        if time_insertion < time_sorted:
            print("Result: Insertion Sort is faster.\n")
        else:
            print("Result: sorted() is faster.\n")

    print("--- Tests Completed ---")