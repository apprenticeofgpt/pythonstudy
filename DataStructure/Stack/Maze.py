class Stack:
  def __init__(self):
    self.lst=[]
  def isEmpty(self):
    return len(self.lst)==0
  def push(self,item):
    self.lst+=[item]
  def pop(self):
    if not self.isEmpty():
      item=self.lst[-1]
      del self.lst[-1]
      return item
  def peek(self):
    if not self.isEmptyy():
      return self.lst[-1]
  def clear(self):
    self.lst=[]
maze = [
    ['1', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]
MAZE_SIZE = 6
s=Stack()
s.push((1,0))

visited = [] # 방문했던 위치 저장

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while not s.isEmpty():
  y, x = s.pop() # 현재 위치
  visited.append((y, x))
  print(f'current location: ({y}, {x})')
  print(f'stack: {s.lst}')

  if maze[y][x] == 'x':
    print("found path")
    break


  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]

    if 0 <= ny < MAZE_SIZE and 0 <= nx < MAZE_SIZE:
      if maze[ny][nx] in ('0', 'x') and (ny, nx) not in visited:
        s.push((ny, nx))
