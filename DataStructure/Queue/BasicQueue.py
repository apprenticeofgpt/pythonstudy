class custom_queue:
  def __init__(self):
    self.lst=[]
  def isEmpty(self):
    return len(self.lst)==0
  def enqueue(self,items):
    self.lst.append(items)
  def dequeue(self):
    if not self.isEmpty():
      return self.lst.pop(0)
  def peek(self):
    if not self.isEmpty():
      return self.lst[-1]
  def size(self):
    return len(self.lst)
  def clear(self):
    self.lst=[]

cq=custom_queue()
for i in range(10):
  cq.enqueue(i)
print(cq.lst)