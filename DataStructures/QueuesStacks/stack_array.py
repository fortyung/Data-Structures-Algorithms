class Stack:
    def __init__(self) -> None:
        self.top = []

    def peek(self):
        return self.top[-1]

    def push(self, value):
        self.top.append(value)
        return self.top

    def pop(self):
        itemToDel = self.top.pop(-1)
        return itemToDel

    def __repr__(self) -> str:
        return str(self.top)


obj = Stack()
obj.push("goole")
obj.push("udemy")
obj.push("youtube")
# print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.pop())

print(obj)
