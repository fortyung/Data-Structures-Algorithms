class Node:
    def __init__(self, value) -> None:
        self.value = {"value": value, "previous": None, "next": None}


class DoublyLinkedList(Node):
    """
    A class representing a custom Doubly Linked List (LL).

    Attributes:
        Value(any): The first item in the LL.

    Methods:
        append(value): Appends a new value to the end of the list and and points its to the value before and after it.
        prpend(value): Appends a new value to the start of the list.
        insert(index, value): inserts a value at a specific index and points its to the value before and after it.
        __traverse(index): Loops to a particular index.
        remove(index): Removes a value at the index
        printList(): Outputs an array of the values.

    """

    def __init__(self, value) -> None:
        super().__init__(value)
        self.head = {"value": value, "previous": None, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        newNode.value["previous"] = self.tail  # Difference
        self.tail["next"] = newNode.value
        self.tail = newNode.value
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        self.head["previous"] = newNode.value
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

        newNode.value["previous"] = leader

        leader["next"] = newNode.value

        hold["previous"] = newNode.value

        newNode.value["next"] = hold
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.traverse(1)
        else:
            leader = self.traverse(index - 1)
            itemTodel = leader["next"]

            hold = itemTodel["next"]
            hold["previous"] = leader
            leader["next"] = hold

            self.length -= 1

    def printList(self):
        array = []
        currentNode = self.head

        while currentNode != None:
            array.append(currentNode["value"])
            currentNode = currentNode["next"]
        return array

    def traverse(self, index):
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode["next"]
        return currentNode

    def __repr__(self):
        return f"head: {self.head},\n\ttail: {self.tail},\n\tlength: {self.length}"


obj = DoublyLinkedList(10)

obj.append(16)
obj.prepend(22)

obj.insert(1, 99)

print(obj.printList())

obj.remove(2)

print(obj.printList())

print(obj)
