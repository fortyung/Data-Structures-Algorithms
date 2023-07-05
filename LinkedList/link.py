class Node:
    def __init__(self, value) -> None:
        self.value = {"value": value, "next": None}


class LinkedList(Node):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail["next"] = newNode.value
        self.tail = newNode.value
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.value["next"] = self.head
        self.head = newNode.value
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)

        newNode = Node(value)
        leader = self.traverse(index - 1)
        hold = leader["next"]
        leader["next"] = newNode.value
        newNode.value["next"] = hold
        self.length += 1

    def traverse(self, index):
        # count = 0
        # currentNode = self.head

        # while count != index:
        #     currentNode = currentNode["next"]
        #     count += 1
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode["next"]
        return currentNode

    def remove(self, index):
        if index == 0:
            self.head = self.traverse(1)
        else:
            # itemToDel = self.traverse(index - 1)
            # leader = self.traverse(index - 2)

            # hold = itemToDel["next"]
            # leader["next"] = hold

            leader = self.traverse(index - 1)
            itemTodel = leader["next"]

            hold = itemTodel["next"]

            leader["next"] = hold

            self.length -= 1

    def printList(self):
        array = []
        currentNode = self.head

        while currentNode != None:
            array.append(currentNode["value"])
            currentNode = currentNode["next"]
        return array

    def __repr__(self):
        return f"head: {self.head},\n\ttail: {self.tail},\n\tlength: {self.length}"


obj = LinkedList(10)

obj.append(16)
obj.prepend(14)
obj.prepend(20)
obj.append(5)


# obj.insert(1, 99)
print(obj.printList())

obj.remove(0)
print(obj.printList())

# print(obj)
