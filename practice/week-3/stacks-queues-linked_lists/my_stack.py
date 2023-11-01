"""Stack"""


class Stack:
    """stack!"""

    def __init__(self):
        self.base = []

    def push(self, item):
        """push"""
        self.base.append(item)

    def pop(self):
        """pop"""
        self.base.pop()

    def peek(self):
        """peek"""
        if len(self.base) == 0:
            return None

        return self.base[-1]


def print_base(stack):
    print("stack base: ", stack.base)


my_stack = Stack()
my_stack.push("hello")
my_stack.push("world")
print_base(my_stack)
print(my_stack.peek())
print_base(my_stack)


# my_stack.pop()
# print_base(my_stack)

# print(my_stack.peek())

# my_stack.pop()
# print_base(my_stack)
