# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I learned how to implement linear and binary searches as well as the benefits and downsides of both. 
2. What challenges did you encounter, and how did you overcome them?
One challenge I encountered was trying to visibly show the difference in the amount of iterations a loop runs when using either search method. I decided to implement a counter that displays the amount of iterations after the search has finished. 
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
Binary search can only be used when you have a sorted list and is more efficient especially as datasets increase compared to linear search as binary search operates at a O(log n), while linear search has a O(n) runtime. Both have the same best case runtime at O(1) if the element is in the beginning for linear search and if the element is at the middle of the list for binary search. Some tradeoffs would be that you have a more efficient search algorithm when using binary, but at the cost of having to maintain a sorted list. Linear search is best for small or unsorted lists, while binary search excels at large sorted lists. 