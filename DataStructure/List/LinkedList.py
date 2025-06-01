class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

sl = SinglyLinkedList()

for i in range(5):     
    sl.add_front(i)

lst = []
curr = sl.head
while curr:
    lst.append(curr.data)
    curr = curr.next

print(lst)
