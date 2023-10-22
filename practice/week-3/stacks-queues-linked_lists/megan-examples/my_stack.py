# from my_node import Node


# class Stack:
#     """Implementing a stack data structure with methods for push, pop, peek, size, and is_empty"""

#     def __init__(self):
#         self.head = None

#     def __repr__(self):
#         return f"| {self.head if self.head is not None else ''} <>"

#     def __iter__(self):
#         self.n = self.head
#         return self

#     def __next__(self):
#         if self.n is not None:
#             value = self.n.value
#             self.n = self.n.next
#             return value
#         else:
#             raise StopIteration


def countdown(n):
    if n != 1:
        countdown(n - 1)
    print(n)


countdown(10)
