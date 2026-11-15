"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #This has an O(n) time complexity because in the worst case and O(1) for best case if its the first element, we may have to check every element in the list to find the target or determine that it is not present.
    iteration_count = 0  # To count the number of iterations
    for (index, value) in enumerate(lst):   
        iteration_count += 1 # Count each iteration of the loop
        if value == target:
            print(f"Linear search iterations: {iteration_count}")
            return index  # Target found, return its index
    print(f"Linear search iterations: {iteration_count}")
    return -1  # Target not found, return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # This has an O(log n) time complexity because with each iteration, the search space is roughly halved, allowing us to quickly narrow down the possible locations of the target.
    # One important note is that binary search requires the list to be sorted beforehand, as it relies on the order of elements to eliminate half of the search space in each iteration.
    left, right = 0, len(lst) - 1
    iteration_count = 0  # To count the number of iterations
    while left <= right:
        iteration_count += 1
        mid = (left + right) // 2  # Find the middle index
        if lst[mid] == target:
            print(f"Binary search iterations: {iteration_count}")
            return mid  # Target found, return its index
        elif lst[mid] < target:
            left = mid + 1  # Target is in the right half, adjust left boundary
        else:
            right = mid - 1  # Target is in the left half, adjust right boundary
    print(f"Binary search iterations: {iteration_count}")
    return -1  # Target not found, return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_dataset = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7
    target_not_found = 4
    linear_result = linear_search(small_dataset, target_value)
    binary_result = binary_search(small_dataset, target_value)
    print(f"Linear search result for {target_value}: {linear_result}")
    print(f"Binary search result for {target_value}: {binary_result}")
    linear_result_not_found = linear_search(small_dataset, target_not_found)
    binary_result_not_found = binary_search(small_dataset, target_not_found)
    print(f"Linear search result for {target_not_found}: {linear_result_not_found}")
    print(f"Binary search result for {target_not_found}: {binary_result_not_found}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # As datasets grow in size, binary search becomes more efficient than linear search because it reduces the number of comparisons needed to find the target value. While linear search checks each element one by one, binary search eliminates half of the remaining elements with each comparison, leading to significantly fewer iterations in larger datasets.
    large_dataset = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
    target_value = 21
    target_not_found = 20
    linear_result = linear_search(large_dataset, target_value)
    binary_result = binary_search(large_dataset, target_value)
    print(f"Linear search result for {target_value}: {linear_result}")
    print(f"Binary search result for {target_value}: {binary_result}")
    linear_result_not_found = linear_search(large_dataset, target_not_found)
    binary_result_not_found = binary_search(large_dataset, target_not_found)
    print(f"Linear search result for {target_not_found}: {linear_result_not_found}")
    print(f"Binary search result for {target_not_found}: {binary_result_not_found}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Value at the first position
    edge_case_first = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_first = 10
    linear_result_first = linear_search(edge_case_first, target_first)
    binary_result_first = binary_search(edge_case_first, target_first)
    print(f"Linear search result for {target_first}: {linear_result_first}")
    print(f"Binary search result for {target_first}: {binary_result_first}")
    # Search result for linear takes only 1 iteration to find the target at the first position, while binary search takes 3 iterations to find the target at the first position.

    # Value at the last position
    edge_case_last = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_last = 100
    linear_result_last = linear_search(edge_case_last, target_last)
    binary_result_last = binary_search(edge_case_last, target_last)
    print(f"Linear search result for {target_last}: {linear_result_last}")
    print(f"Binary search result for {target_last}: {binary_result_last}")
    # Search result for linear takes 10 iterations to find the target at the last position, while binary search takes 4 iterations to find the target at the last position.




if __name__ == "__main__":
    main()