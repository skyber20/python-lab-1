class Stack:
    def __init__(self):
        self.items: list = []

    def push(self, elem: int | float):
        self.items.append(elem)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0