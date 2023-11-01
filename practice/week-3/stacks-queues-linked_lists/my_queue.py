""" Queue """

# enqueue - add an item to the beginning
# dequeue - remove an item from the end and return that item
# peek - return the value of the item currently at the beginningprint_base(my_stack)


class Queue:
    """Queue class"""

    def __init__(self):
        self._q = []

    def enqueue(self, item):
        """enqueue - add an item to the beginning"""
        self._q.insert(0, item)

    def dequeue(self):
        """
        dequeue - remove an item from the end and return that item
        """
        return self._q.pop()

    def peek(self):
        """peek - return the item at the head of the queue"""

        return self._q[-1]


my_q = Queue()

my_q.enqueue("first pizza order")
my_q.enqueue("second pizza order")
my_q.enqueue("third pizza order")

print(my_q._q)

print(my_q.dequeue())
print(my_q._q)

print(my_q.peek())
