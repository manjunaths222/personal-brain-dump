---
title: "Python"
---

Python

Resources:
- https://www.interviewbit.com/python-interview-questions/
- https://www.geeksforgeeks.org/python-interview-questions/
- https://www.datacamp.com/blog/top-python-interview-questions-and-answers

Data Types:
- int, float, complex, str, bool
- list (mutable), tuple (immutable), range
- set (unordered, unique), dict (key-value)

Control Flow: if/elif/else, for, while
List Comprehension: [x**2 for x in range(1,6)]

Functions:
- def, lambda
- *args (variable-length), **kwargs (key-value)

OOP:
- class, __init__, self
- Inheritance: super().__init__()
- Polymorphism: override methods

File Handling:
```python
with open("file.txt", "w") as f: f.write("Hello")
with open("file.txt", "r") as f: content = f.read()
```

Exception Handling: try/except/finally

Decorators:
```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hello(): print("Hello!")
```

Generators: use yield instead of return (lazy evaluation)

Memory Management:
- Private heap space (not directly accessible)
- PyMalloc: specialized allocator for small objects
- Reference Counting: memory freed when ref count hits 0
- Cyclic GC: detects reference cycles

Shallow vs Deep Copy:
- Shallow copy: copies reference addresses for nested objects
- Deep copy: recursively duplicates all nested objects
```python
from copy import copy, deepcopy
list_2 = copy(list_1)   # shallow
list_3 = deepcopy(list_1)  # deep
```

Data Structures Comparison:
| Structure | Mutable | Ordered | Duplicates | Use Case |
|-----------|---------|---------|------------|----------|
| list | Yes | Yes | Yes | Ordered collections, modification |
| tuple | No | Yes | Yes | Fixed data, hashable keys |
| set | Yes | No | No | Unique elements, fast lookup |
| dict | Yes | Yes | No (keys) | Key-value mapping |

Set Operations:
```python
set1 | set2  # Union
set1 & set2  # Intersection
set1 - set2  # Difference
```
