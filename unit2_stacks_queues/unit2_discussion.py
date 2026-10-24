"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque



class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        self._items.pop() if self._items else None

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        self._items.peek() if self._items else None

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        self._items.is_empty()


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        return self._items.popleft() if self._items else None

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        return self._items[0] if self._items else None

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

stack = Stack()
print("Initial stack contents: ", stack._items)
stack.push(1)
print("Stack after pushing 1: ", stack._items)
stack.push(2)
print("Stack after pushing 2: ", stack._items)
stack.push(3)
print("Stack after pushing 3: ", stack._items)
stack.push(4)
print("Stack after pushing 4: ", stack._items)

print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

print("Current stack contents (from bottom to top):")
# For loop to display stack contents with clear indication of top and bottom
for i in stack._items:
    if i == stack._items[0]:
        print(i, "<-- Bottom of Stack")
    elif i == stack._items[-1]:
        print(i, "<-- Top of Stack")
    else:
        print(i)

stack.pop()
print("Stack after popping the top item:", stack._items)
stack.pop()
print("Stack after popping the next item:", stack._items)
stack.pop()
print("Stack after popping the next item:", stack._items)
stack.pop()
print("Stack after popping all items:", stack._items)
print("Attempt to pop from an empty stack:", stack.pop())  # Attempt to pop from an empty stack
print("Peek at the top of the stack:", stack.peek())  # Attempt to peek at an empty stack
stack.push(5)
print("Stack after pushing one item:", stack._items)
stack.pop()
print("Stack after popping the single item:", stack._items)


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

if __name__ == "__main__":
    main()
    queue = Queue()
    print("Initial queue contents: ", list(queue._items))
    queue.enqueue(1)
    print("Queue after enqueueing 1: ", list(queue._items))
    queue.enqueue(2)
    print("Queue after enqueueing 2: ", list(queue._items))
    queue.enqueue(3)
    print("Queue after enqueueing 3: ", list(queue._items))
    queue.enqueue(4)
    print("Queue after enqueueing 4: ", list(queue._items))
    queue.dequeue()
    print("Queue after dequeueing 1: ", list(queue._items))
    queue.dequeue()
    print("Queue after dequeueing 2: ", list(queue._items))
    queue.dequeue()
    print("Queue after dequeueing 3: ", list(queue._items))
    queue.dequeue()
    print("Queue after dequeueing 4: ", list(queue._items))
    print("Attempt to dequeue from an empty queue:", queue.dequeue())  # Attempt to dequeue
    print("Front of the queue:", queue.front())  # Attempt to view front of an empty queue
    queue.enqueue(5)
    print("Queue after enqueueing one item:", list(queue._items))
    queue.dequeue()
    print("Queue after dequeueing the single item:", list(queue._items))
