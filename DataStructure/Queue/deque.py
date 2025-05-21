"""
배열 기반 원형 덱
"""
class deque:
  def __init__(self,maxsize=6):
    self.maxsize=maxsize
    self.array=[None]*maxsize
    self.front=0
    self.rear=0
  def isEmpty(self):
    return self.front==self.rear
  def isFull(self):
    return self.front==(self.rear+1)%self.maxsize
  def push_front(self,item):
    if not self.isFull():
      self.front = (self.front - 1 + self.maxsize) % self.maxsize
      self.array[self.front]=item
  def pop_front(self):
    if not self.isEmpty():
      item=self.array[self.front]
      self.array[self.front] = None
      self.front = (self.front + 1) % self.maxsize
      return item
  def push_rear(self,item):
    if not self.isFull():
      self.array[self.rear]=item
      self.rear = (self.rear + 1) % self.maxsize
  def pop_rear(self):
    if not self.isEmpty():
      self.rear = (self.rear - 1 + self.maxsize) % self.maxsize
      item = self.array[self.rear]
      self.array[self.rear] = None
      return item