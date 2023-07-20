class HashTable:

    """
    A class representing a custom hash table.

    Attributes:
        size (int): The size of the object.

    Methods:
        set(key,value): Adds new entries to the hash table.
        _hash(key): Creates a hash code for the key (an address).
        get(key): Retrivies the value for a specified key.
        keys(): Retrivies all keys.
        values(): Retrivies all values.

    """

    def __init__(self, size) -> None:
        self.data = [None] * size 

    # def set(self, key, value): # O(1)
    #     address = self.hash(key)

    #     if self.data[address] != None:
    #         if isinstance(self.data[address][0], list):
    #             self.data[address].append([key, value])
    #         else:
    #             self.data[address] = [ [self.data[address][0], self.data[address][1]], [key, value] ]
    #     else:
    #         self.data[address] = [key, value]
    #     return self.data

    def set(self, key, value): # O(1)
        address = self._hash(key)
        if self.data[address] == None:
            self.data[address] = []
              
        self.data[address].append([key, value])
        return self.data
    
    def _hash(self, hkey): # O(1)
        i = 0
        hash = 0

        while i < len(hkey):
            hash = (hash + ord(hkey[i]) * i) % len(self.data)
            i += 1
        return hash

    def get(self, gkey): # O(1)
        address = self._hash(gkey)

        for i in range(len(self.data[address])):
            if gkey in self.data[address][i]:
                return self.data[address][i][1]
            
        return False
    
    def keys(self):
        key_lis = []
        
        for i in range(len(self.data)):
            if self.data[i]:
                if len(self.data[i]) < 1:
                    key_lis.append(self.data[i][0][0])
                else:
                    for item in self.data[i]:
                        key_lis.append(item[0])
                
                # ''' incase we have elements sharing the same address '''
 
        return key_lis
 
    def values(self):
        values_lis = []

        for i in range(len(self.data)):
            if self.data[i]:
                # if len(self.data[i]) < 1:
                    values_lis.append(self.data[i][0][1])
                # else:
                #     for item in self.data[i]:
                #         values_lis.append(item[1])
                
        return values_lis
        

obj = HashTable(2)
obj.set('name', 'fortune')
obj.set('nami', 'young')
obj.set('nams', 'sis')
obj.set('namy', 'bob')


# print(obj.hash('name'))
obj.set('age', 22)
# obj.set('food', 'rice')
 

# print(obj.get('age'))
# print(obj.data)
print(obj.keys())
print(obj.values())
