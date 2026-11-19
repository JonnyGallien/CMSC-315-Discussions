"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    hash_table = {}
    hash_table["key1"] = "value1"
    hash_table["key2"] = "value2"
    hash_table["key3"] = "value3"
    hash_table["key4"] = "value4"
    hash_table["key5"] = "value5"
    # A dictionary behaves like a hash table because it allows for fast lookups, insertions, and deletions of key-value pairs. 
    # Each key is unique and maps to a specific value, similar to how a hash table uses a hash function to map keys to values.
    print("Created hash table:")
    for key, value in hash_table.items():
        print(f"  {key}: {value}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    value1 = hash_table.get("key1")
    value2 = hash_table.get("key2")
    print(f"Lookup result for 'key1': {value1}")
    print(f"Lookup result for 'key2': {value2}")
    # The lookup works by using the key to access the corresponding value in the dictionary. 
    # The dictionary uses a hash function to quickly locate the value associated with the given key.

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Dictionary before update:")
    for key, value in hash_table.items():
        print(f"  {key}: {value}")
    hash_table["key1"] = "new_value1"
    print("Dictionary after update:")
    for key, value in hash_table.items():
        print(f"  {key}: {value}")
    # When a key that already exists in the dictionary is assigned a new value, the old value is replaced with the new one.

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Dictionary before deletion:")
    for key, value in hash_table.items():
        print(f"  {key}: {value}")
    del hash_table["key2"]
    print("Dictionary after deletion:")
    for key, value in hash_table.items():
        print(f"  {key}: {value}")
    # When a key-value pair is deleted from the dictionary, the key is removed along with its associated value.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Lookup a missing key
    print("Edge Case 1: Attempting to lookup a missing key:")
    missing_key_lookup = hash_table.get("missing_key")
    print(f"Lookup result for 'missing_key': {missing_key_lookup}")
    # When looking up a missing key, the result is None because the key does not exist
    print()

    # Edge Case 2: Delete a missing key safely
    print("Edge Case 2: Attempting to delete a missing key safely:")
    try:
        del hash_table["missing_key"]
    except KeyError:
        print("KeyError: 'missing_key' does not exist in the dictionary. Deletion skipped.")
    # When attempting to delete a missing key, a KeyError is raised. We can use a try-except block to handle this error avoiding a program crash.
    print()

    # Edge Case 3: Update a missing key
    print("Edge Case 3: Attempting to update a missing key:")
    hash_table["missing_key"] = "new_value"
    print(f"Updated 'missing_key' to: {hash_table['missing_key']}")
    # When updating a missing key, a new key-value pair is created in the dictionary.
    print()

    # Edge case 4: Lookup a missing key in an empty dictionary
    empty_dict = {}
    print("Edge Case 4: Attempting to lookup a missing key in an empty dictionary:")
    missing_key_lookup = empty_dict.get("missing_key")
    print(f"Lookup result for 'missing_key': {missing_key_lookup}")
    # When looking up a missing key in an empty dictionary, the result is None because the key does not exist.





if __name__ == "__main__":
    main()