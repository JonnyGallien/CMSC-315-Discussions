# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

I learned how to implement and use a BST and recursive tree operations. BST can help reduce the number of operations to search through data with a balanced search tree having a time of O(log n) and an unbalanced tree having a worst case of O(n).

One of the challenges I encountered was understanding how recursion works by inserting and searching through nodes. I initially had some difficulty understanding how each recursive call moves through the tree. A lot of the Zybook images really helped my understanding by showing trees before and after as well or balanced and unbalanced trees. 

BST's use ordering to improve efficiency by placing smaller values in the left subtree and larger values in the right subtree. This allows searches to eliminate entire subtrees at every comparison instead of checking every single element. Compared to a standard list or an unsorted array a balanced search tree can locate values much faster. However, the speed depends on keeping the binary tree as balanced as possible.