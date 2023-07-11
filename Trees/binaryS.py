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
                    currentNode = currentNode.left1
                elif value > currentNode.value:
                    currentNode = currentNode.right
                elif value == currentNode.value:
                    return currentNode
            return False

    def remove(self, value):  # Needs some work lol
        if not self.root:
            return False

        currentNode = self.root
        parentNode = None

        while currentNode:
            # Finding the Node.
            if value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value < currentNode.value:
                parentNode = currentNode
                currentNode.left
            elif value == currentNode.value:
                # We have a match.

                # No right child (value is the root Node).
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    # Update the root node to the value on the left Node.
                    else:
                        # make the left the parent node
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left

                        # make the right the parent node
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right

                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if not parentNode:
                        self.root = currentNode.right
                    else:
                        # make the left the parent node
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left

                        # make the right the parent node
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                else:
                    # Right's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right

                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost

                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                return True


def traverse(node):
    if node is None:
        return None
    tree = {"value": node.value}
    tree["left"] = traverse(node.left) if node.left is not None else None
    tree["right"] = traverse(node.right) if node.right is not None else None
    return tree


# Create the tree and insert nodes
tree = BinarySearchTree()
tree.insert(38)
tree.insert(20)
tree.insert(70)
tree.insert(8)
tree.insert(31)
tree.insert(30)
tree.insert(37)
tree.insert(35)
tree.insert(36)
print(tree.remove(0))
# print(tree.lookup(0))

# Convert the tree to JSON
# json_string = json.dumps(traverse(tree.root))
# print(json_string)
