class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value if self.first else None

    def enqueue(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.length += 1
        return newNode.value

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None

        itemToDel = self.first.value
        self.first = self.first.next
        self.length -= 1

        return itemToDel


obj = Queue()
obj.enqueue("google")
obj.enqueue("youtube")
obj.enqueue("udemy")
print(obj.peek())

print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
