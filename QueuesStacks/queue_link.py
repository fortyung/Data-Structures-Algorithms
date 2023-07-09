class Node:
    def __init__(self, value) -> None:
        self.value = {"value": value, "next": None}


class Stack:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first, self.last

    def enqueue(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.first = newNode.value
            self.last = self.first
        else:
            self.last["next"] = newNode.value
            self.last = newNode.value

        self.length += 1
        return self.first

    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.last = None

        self.first = self.first["next"]
        self.length -= 1

        return self.first, self.last


obj = Stack()
obj.enqueue("google")
obj.enqueue("youtube")
obj.enqueue("udemy")
print(obj.peek())

print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
