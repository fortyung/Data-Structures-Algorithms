class Node:
    def __init__(self, value) -> None:
        self.value = {"value": value, "next": None}


class LinkedList(Node):
    """
    A class representing a custom Linked List (LL).

    Attributes:
        Value(any): The first item in the LL.

    Methods:
        append(value): Appends a new value to the end of the list and points its to the value before it.
        prpend(value): Appends a new value to the start of the list.
        insert(index, value): inserts a value at a specific index and points its to the value before it.
        __traverse(index): Loops to a particular index.
        remove(index): Removes a value at the index
        printList(): Outputs an array of the values.
        reverse(): Reverses the linked list.

    """

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
        leader = self.__traverse(index - 1)
        hold = leader["next"]
        leader["next"] = newNode.value
        newNode.value["next"] = hold
        self.length += 1

    def __traverse(self, index):
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
            self.head = self.__traverse(1)
        else:
            leader = self.__traverse(index - 1)
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

    def reverse(self):
        if self.head["next"] == None:
            return self.head

        first = self.head
        self.tail = self.head
        second = first["next"]

        while second != None:
            temp = second["next"]
            second["next"] = first
            first = second
            second = temp

        self.head["next"] = None
        self.head = first

    def __repr__(self):
        return f"head: {self.head},\n\ttail: {self.tail},\n\tlength: {self.length}"


obj = LinkedList(10)

obj.append(16)
obj.prepend(14)
# obj.prepend(20)
# obj.append(5)


# obj.insert(1, 99)
print(obj.printList())

# obj.remove(0)
obj.reverse()
print(obj.printList())

print(obj)
