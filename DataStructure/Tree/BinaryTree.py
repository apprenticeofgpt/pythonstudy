class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 전위 순회: Root → Left → Right
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# 중위 순회: Left → Root → Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# 후위 순회: Left → Right → Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
