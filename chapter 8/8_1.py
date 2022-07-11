# implement a stack with max API

# O(N) space
# O(1) time

class Stack:

    def __init__(self):
        self.elements = []
        self.max = []

    def empty(self):
        return len(self.elements) == 0

    def pop(self):
        self.max.pop()
        return self.elements.pop()

    def push(self, new_elem):
        self.elements.append(new_elem)
        self.max.append(max(self.max[-1], new_elem))

    def get_max(self):
        return self.max[-1]