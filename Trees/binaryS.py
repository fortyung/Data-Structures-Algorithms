import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if not self.root:
            self.root = newNode

        else:
            currentNode = self.root

            while True:
                if value > currentNode.value:
                    # Right
                    if not currentNode.right:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right

                else:
                    if value < currentNode.value:
                        # Left
                        if not currentNode.left:
                            currentNode.left = newNode
                            return self
                        currentNode = currentNode.left

    def lookup(self, value):
        if not self.root:
            return False

        else:
            currentNode = self.root
            while currentNode:
                if value < currentNode.value:
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    currentNode = currentNode.right
                elif value == currentNode.value:
                    return currentNode
            return False


def traverse(node):
    if node is None:
        return None
    tree = {"value": node.value}
    tree["left"] = traverse(node.left) if node.left is not None else None
    tree["right"] = traverse(node.right) if node.right is not None else None
    return tree


# Create the tree and insert nodes
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.lookup(0))

# Convert the tree to JSON
json_string = json.dumps(traverse(tree.root))
print(json_string)
