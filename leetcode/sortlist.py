# class Solution:
#     def sortList(self, head: ListNode) ->  ListNode:
#         if not head or not head.next:
#             return head

#         # Split the list into two halfs
#         left = head
#         right = self.getMid(head)
#         tmp = right.next
#         right.next = None
#         right = tmp

#         left = self.sortList(left)
#         right = self.sortList(right)

#         return self.merge(left, right)

#     def getMid(self, head):
#         slow = head
#         fast = head.next

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

#     # Merge the list
#     def merge(self, list1, list2):
#         newHead = tail = ListNode()
#         while list1 and list2:
#             if list1.val > list2.val:
#                 tail.next = list2
#                 list2 = list2.next
#             else:
#                 tail.next = list1
#                 list1 = list1.next
#             tail = tail.next

#         if list1:
#             tail.next = list1
#         if list2:
#             tail.next = list2

#         return newHead.next


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()

first_node = Node("a")
llist.head = first_node

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)
