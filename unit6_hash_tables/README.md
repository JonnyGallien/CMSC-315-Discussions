# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
The concepts and skills I learned while completing this assignment were how to work with a Python dictionary. I learned how to perform insert, retrieve, update, and remove operations on dictionaries. I also learned how hashing works.

2. What challenges did you encounter, and how did you overcome them?
One difficulty I had during this assignment was on my second edge case testing. It took me a minute to figure out that the program terminates without implementing a try/except block. I changed the implementation to include that so that the program can fully run. 
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
Hash tables work by using a hash function to return the bucket index that the item will be assigned to. A collision occurs when two separate keys have the same result from a hash function. Hash tables improve efficiency by reducing lookup times in larger datasets by giving the system a good idea where to start instead of following a linear search approach where you start at the beginning or end and run all the way through the list. Hash function searches when implemented correctly with no collisions have a run time complexity of O(1).