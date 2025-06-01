class Node:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, priority, data):
        new_node = Node(priority, data)

        # 큐가 비었거나 새 노드의 우선순위가 가장 높을 경우 (head 교체)
        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            # 삽입 위치를 찾는다
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def pop(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        return node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(f"[{current.priority}] {current.data}", end=" -> ")
            current = current.next
        print("None")
