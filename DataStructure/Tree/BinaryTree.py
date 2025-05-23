class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
first_node=node(0)
second_node=node(1)
third_node=node(2)
fourth_node=node(3)

first_node.left=second_node
first_node.right=third_node
second_node.left=fourth_node

print("pre:")
preorder(first_node)

print("\nin:")
inorder(first_node)

print("\npost:")
postorder(first_node)
