class cirucular_queue:
  def __init__(self):
    self.qsize=5
    self.front=0
    self.rear=0
    self.items=[None]*self.qsize
  def isEmpty(self):
    return self.rear==self.front
  def clear(self):
    self.rear=self.front
  def isFull(self):
    return self.front==(self.rear+1)%self.qsize
  def enqueue(self,items):
    if not self.isFull():
      self.rear=(self.rear+1)%self.qsize
      self.items[self.rear]=items
  def dequeue(self):
    if not self.isEmpty():
      next_front = (self.front + 1) % self.qsize
      item = self.items[next_front]
      self.items[next_front] = None  # 먼저 값을 저장한 다음 삭제
      self.front = next_front        # 그 후에 front 이동
      return item
  def peek(self):
    if not self.isEmpty():
      return self.items[(self.front+1)%self.qsize]
  def size(self):
    return (self.front+self.qsize)%self.qsize