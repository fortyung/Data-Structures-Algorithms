class Graph:
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            return False

        self.adjacentList[node] = []
        self.numberOfNodes += 1

        return self.adjacentList

    def addEdge(self, node1, node2):
        if node1 and node2 not in self.adjacentList:
            return False

        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

        return self.adjacentList

    def showConnections(self):
        allNodes = list(self.adjacentList.keys())

        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += str(vertex) + " "
            print(str(node) + "-->" + str(connections))


obj = Graph()
obj.addVertex(0)
obj.addVertex(1)
obj.addVertex(2)
obj.addVertex(3)
obj.addVertex(4)
obj.addVertex(5)
obj.addVertex(6)

obj.addEdge(3, 1)
obj.addEdge(3, 4)
obj.addEdge(4, 2)
obj.addEdge(4, 5)
obj.addEdge(1, 2)
obj.addEdge(1, 0)
obj.addEdge(0, 2)
obj.addEdge(6, 5)

print(obj.showConnections())

print(obj.addEdge(0, 1))
