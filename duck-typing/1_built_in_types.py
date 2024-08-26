# Approaches to support duck typing


# 1. Python extensively uses duck typing in built-in types
# built-in types support:
# iteration
# indexing
# slicing
# concatenating
# finding length
# reversing
# sorting
# ...

numbers = [1, 2, 3]
person = ("Jane", 25, "Python Dev")
letters = "abc"
ordinals = {"one": "first", "two": "second", "three": "third"}
even_digits = {2, 4, 6, 8}
collections = [numbers, person, letters, ordinals, even_digits]

for collection in collections:
    for value in collection:
        print(value)

# 2. Custom class and regular methods
# see example.py

# 3. Custom class using special methods and protocols

from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    def __iter__(self):
        return iter(self._elements)

    def __len__(self):
        return len(self._elements)

    def __reversed__(self):
        return reversed(self._elements)

    def __contains__(self, element):
        return element in self._elements
    


# >>> from queues import Queue

# >>> queue = Queue()
# >>> queue.enqueue(1)
# >>> queue.enqueue(2)
# >>> queue.enqueue(3)

# >>> [item for item in queue]
# [1, 2, 3]

# >>> len(queue)
# 3
# >>> list(reversed(queue))
# [3, 2, 1]

# >>> 2 in queue
# True
# >>> 6 in queue