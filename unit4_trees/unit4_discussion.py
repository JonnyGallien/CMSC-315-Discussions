"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If the value is equal we do not insert duplicates.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        if self.root is None:
            return False
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    bst = BST()
    unbalanced_BST = BST()
    # An unordered list of values to insert into the BST.
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
    unbalanced_values = [5, 10, 15, 25, 35, 45, 55]
    for value in unbalanced_values:
        unbalanced_BST.insert(value)

    print("Values inserted:", values)
    print("Unbalanced values inserted:", unbalanced_values)
    # A BST reduces search space efficiently by eliminating a subtree at each comparison. 
    # A balanced BST ensures that the height of the tree is minimized, leading to O(log n) search time on average, 
    # while an unbalanced BST can degrade to O(n) in the worst case.
    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    inorder_values = bst.inorder()
    print("In-order traversal results:", inorder_values)
    # In-order traversal produces sorted output in a BST because it visits nodes in the order of left subtree, current node, 
    # and right subtree, which respects the BST property that left children are smaller than the parent node and right children are larger.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Search for values that exist
    print("Searching for 40:", bst.search(40))
    # It takes 3 comparisons to find 40 in the BST: 50 -> 30 -> 40.
    print("Searching for 70:", bst.search(70))
    # It takes 2 comparisons to find 70 in the BST: 50 -> 70.

    # Search for values that do not exist
    print("Searching for 25:", bst.search(25))
    # It takes 3 comparisons to determine that 25 is not in the BST: 50 -> 30 -> 20 (and then it would check the right child of 20, which is None).
    print("Searching for 90:", bst.search(90))
    # It takes 3 comparisons to determine that 90 is not in the BST: 50 -> 70 -> 80 (and then it would check the right child of 80, which is None).
    print("searching for 55 in unbalanced BST:", unbalanced_BST.search(55))
    # It takes 7 comparisons to find 55 in the unbalanced BST: 5 -> 10 -> 15 -> 25 -> 35 -> 45 -> 55.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")
    empty_bst = BST()
    print("Searching in an empty BST for 10:", empty_bst.search(10))
    # The search returns False because the tree is empty, and there are no nodes to search through.



if __name__ == "__main__":
    main()