class Recurring:

    def __init__(self, array) -> None:
        self.array = array
        self.data = [None] * len(array) 
        
    def match(self):
        for i in range(len(self.array)):
            if self.array[i] not in self.data:
                self.data[i] = self.array[i]
            else:
                print(self.data)
                return self.array[i]
        return False
    

def recurring(array):
    map = {}

    for i in range(len(array)): 
        if array[i] in map:
            return array[i]
        else:
            map[array[i]] = i
    return False


    

obj = Recurring([5,3,2,3,5])
print(obj.match())

print(recurring([1,3,2,3,1]))