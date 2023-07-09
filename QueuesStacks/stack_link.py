class Node:
    def __init__(self, value) -> None:
        self.value = {"value": value, "next": None}


class Stack(Node):
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)

        if self.top == None:
            self.top = newNode.value
            self.bottom = self.top
        else:
            newNode.value["next"] = self.top
            self.top = newNode.value

        self.length += 1

        return self.top

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.bottom = None

        item = self.top["value"]
        self.top = self.top["next"]
        self.length -= 1

        return item

    def __repr__(self) -> str:
        return f"Top: {self.top}, Bottom: {self.bottom}, Length: {self.length}"


obj = Stack()
obj.push("google")
obj.push("udemy")
print(obj.peek())
print(obj.pop())
print(obj.pop())

# print(obj)
