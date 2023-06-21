class MyArray:
    """
    A class representing a custom array.

    Attributes:
        length (int): The current length of the array.
        data (dict): The dictionary storing the array elements.

    Methods:
        push(item): Adds an item to the end of the array.
        get(index): Retrives items in the array using its index.
        pop(): Removes the last item from the array.
        delete(index): Deletes a specified item in the array using its index.
        __unshift(index): Removes a specified item with its index.


    """

    def __init__(self):
        self.__length = 0  # Encapsulation: The double underscore makes the variable unaccessable outside the class
        self.__data = {}

    def get(self, index):
        if self.__length == 0:
            return None
        return self.__data[index]
        # O(1)

    def push(self, item):
        self.__data[self.__length] = item
        self.__length += 1
        return self.__data
        # O(1)

    def pop(self):
        if self.__length == 0:
            return None
        
        self.__length -= 1
        popped_item = self.__data[self.__length]
        del self.__data[self.__length]
        return popped_item
        # O(1)
    
    def delete(self, index):
        item = self.__data[index]
        self.__unshift(index)
        return item
        # O(n)
    
    def __unshift(self, index): # Abstraction: This class is not accessable outside this class
        for i in range(index, self.__length - 1):
            self.__data[i] = self.__data[i + 1]
        del self.__data[self.__length - 1]
        self.__length -= 1
        # O(n)

    def __repr__(self):
        return str(self.__data)
    
    def infos(self):
        return {'length': self.__length, 'data': self.__data}




    
new_array = MyArray()
new_array.push('hi')
new_array.push('you')
new_array.push('!')
print(new_array.__repr__())

print(new_array.delete(1))

print(new_array.__repr__())


    
# ob1 = MyArray()
# ob1.push('boy')
# print(ob1.push('girl'))
# print(ob1.delete(0))
# ob1.pop()
# print(ob1.push('juice'))



