class MyQueue(object):
    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.front.insert(len(self.front), x)  # Appends to the front array.

    def pop(self):
        """
        :rtype: int
        """
        if not self.back:  # if self.back is None.
            while self.front:
                self.back.insert(0, self.front.pop(0))
        if self.back:
            return self.back.pop()
        return False

    def peek(self):
        """
        :rtype: int
        """
        if not self.back:  # if self.back is None.
            while self.front:
                self.back.insert(0, self.front.pop(0))
        if self.back:
            return self.back[-1]
        return False

    def empty(self):
        """
        :rtype: bool
        """
        return not self.back and not self.front


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push("google")
obj.push("udemy")
obj.push("fish")

param_2 = obj.pop()
obj.push("book")
param_2 = obj.pop()
param_2 = obj.pop()
param_2 = obj.pop()

param_3 = obj.peek()
param_4 = obj.empty()

print(param_2, param_3, param_4)
