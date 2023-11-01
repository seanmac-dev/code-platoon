from my_node import Node
from collections import deque

"""Linked List"""


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)


a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
print(a_list)

# d = deque()
# d.append("Harry")
# d.append("Potter")

# for item in d:
#     print(item)


# """Linked list"""


# class Node:
#     """individual node in our linked list"""

#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return f"{self.value}"


# class LinkedList:
#     """
#     Linked List handler/main class
#     Insert at head of list.
#     If node.next is None it means we are at the end of the list.
#     """

#     def __init__(self):
#         self.head = None

#     def insert(self, value):
#         """insert value as new node into list"""
#         new_node = Node(value)
#         old_node = self.head  # keep track of the old head
#         self.head = new_node
#         self.head.next = old_node  # point new head to old head to add our new node to the head/beginning of list

#     def print_all_items_in_list(self):
#         current = self.head
#         while current is not None:
#             print(current)
#             current = (
#                 current.next
#             )  # At the end of the list, current.next is None, so then current is set to None

#     def search(self, value):
#         """find a node in the list with `value"""


# # test_node = Node("hello world")
# # print(test_node.value)
# # print(test_node.next)

# my_list = LinkedList()

# user = {"name": "Alice", "email": "alice@gmail.com"}

# my_list.insert(user)
# my_list.insert("hello world")
# my_list.insert("goodbye")

# my_list.print_all_items_in_list()
# print(my_list.head)

# print(my_list.head.value)
# print(my_list.head.next.value)
# print(my_list.head.next.next.value)
