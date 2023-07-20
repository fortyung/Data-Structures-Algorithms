class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack(Node):
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value if self.top else None

    def push(self, value):
        newNode = Node(value)

        if self.top == None:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode

        self.length += 1

        return self.top.value

    def pop(self):
        if not self.top:
            return None

        if self.top == self.bottom:
            self.bottom = None

        item = self.top.value
        self.top = self.top.next
        self.length -= 1

        return item

    def __repr__(self) -> str:
        return f"Top: {self.top.value if self.top else None}, Bottom: {self.bottom.value if self.bottom else None}, Length: {self.length}"


obj = Stack()
obj.push("google")
obj.push("udemy")
print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.peek())


# print(obj)
