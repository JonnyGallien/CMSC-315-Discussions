"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    """
    Inserting a value at a specific index in a list shifts all elements
    at that index and beyond to the right, making space for the new value.
    Insertion performance can vary depending on the index:
    - Inserting at the beginning (index 0) requires shifting all elements,
      which can be costly for large lists.
    - Inserting in the middle requires shifting half of the elements on average.
    - Inserting at the end (using append) is generally more efficient, as it
      does not require shifting any elements.
    """
    if 0 <= index <= len(lst):
        lst.insert(index, value)
    else:
        # Index is invalid; do not perform insertion.
        print(f"Index {index} is invalid. No insertion performed.")


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if 0 <= index < len(lst):
        return lst.pop(index)
    else:
        # Index is invalid; return None to indicate that no deletion occurred.
        print(f"Index {index} is invalid. No deletion performed.")
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    if value in lst:
        return lst.index(value)
    else:
        #If value is not found, return -1 to indicate that the search was unsuccessful.
        print(f"Value {value} not found in the list.")
        return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")



    # Create a list with initial values
    newList = [1, 2, 3, 4, 5]
    print("Original list:", newList)

    # Insert a value at the beginning of the list
    newList.insert(0, 0)
    print("After inserting 0 at the beginning:", newList)

    # Insert a value in the middle of the list
    newList.insert(3, 3.5)
    print("After inserting 3.5 at index 3:", newList)

    # Insert a value at the end of the list
    newList.append(6)
    print("After appending 6:", newList)

    # If you want to append to a list using the insert_at function, you can do so by specifying the index as the length of the list.
    insert_at(newList, len(newList), 7)
    print("After inserting 7 at the end using insert_at function:", newList)



    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    deletion_list = [1, 2, 3, 4, 5]
    print("Original list for deletion tests:", deletion_list)

    # Delete an item from the beginning of the list
    removed_value = deletion_list.pop(0)
    print(f"Removed value from the beginning: {removed_value}")
    print("List after deletion from the beginning:", deletion_list)

    # Delete an item from the middle of the list
    removed_value = deletion_list.pop(2)
    print(f"Removed value from the middle: {removed_value}")
    print("List after deletion from the middle:", deletion_list)

    # Delete an item from the end of the list
    removed_value = deletion_list.pop()
    print(f"Removed value from the end: {removed_value}")
    print("List after deletion from the end:", deletion_list)
    #Delete an item from the end of the list using the delete_at function
    removed_value = delete_at(deletion_list, len(deletion_list) - 1)
    print(f"Removed value from the end using delete_at function: {removed_value}")
    print("List after deletion from the end using delete_at function:", deletion_list)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Create a list for searching
    newList = [1, 2, 3, 4, 5]
    print("List for searching:", newList)

    # Search for a value that exists in the list
    search_value_existing = 3
    index_found = newList.index(search_value_existing) 
    print(f"Value {search_value_existing} found at index: {index_found}")
    # Search for a value that exists in the list using the search_value function
    search_result = search_value(newList, search_value_existing)
    print(f"Search result for {search_value_existing}: {search_result}")


    # Search for a value that does not exist in the list. Note there is no error handling here for a nonexisting value in order to display the result of searching for a nonexisting value. This will raise a ValueError if the value is not found.
    search_value_missing = 10
    #Uncomment the following line to see the result of searching for a nonexisting value. It is commented out to avoid the ValueError from stopping the program.
    #nonexisting_search_result = newList.index(search_value_missing)
    #Print statement will not execute due to ValueError raised above.
    #Uncomment the following line to see the result of searching for a nonexisting value. It is commented out to avoid the ValueError from stopping the program.
    #print(f"Value {search_value_missing} not found in the list. Result of searching for nonexisting value: {nonexisting_search_result}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Initial array for edge case testing
    edge_case_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Initial list for edge case testing:", edge_case_list)
    

    # Edge Case 1: Attempt to delete using an invalid index
    invalid_index = 10

    # This is an example of how you would handle incoming values for testing
    print(f"Attempting to delete at invalid index {invalid_index}.")
    if invalid_index < 0 or invalid_index >= len(edge_case_list):
        #Performing the removed_value = edge_case_list.pop(invalid_index) would throw 
        print(f"Index {invalid_index} is invalid. No deletion performed.")
    else:
        removed_value = edge_case_list.pop(invalid_index)
        print(f"Removed value: {removed_value}")
        print("List after deletion:", edge_case_list)

    # Edge Case 2: Insert into a negative index (which is valid in Python, but may not be intended)
    print("\nEdge Case 2: Insert into a negative index.")
    print("Initial list for edge case testing:", edge_case_list)
    negative_index = -1
    value_to_insert = 99
    print(f"Attempting to insert {value_to_insert} at negative index {negative_index}.")
    edge_case_list.insert(negative_index, value_to_insert)
    print("List after insertion:", edge_case_list)

    # Edge Case 3: Search for a missing value
    print("\nEdge Case 3: Search for a missing value.")
    missing_value = 100
    search_result = search_value(edge_case_list, missing_value)
    print(f"Search result for missing value {missing_value}: {search_result}")

    



if __name__ == "__main__":
    main()