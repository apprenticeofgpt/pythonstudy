s_i=input()
numbers=[str(i) for i in range(0,10)]
stck=[]
exp=[]
for i in range(len(s_i)):
  if s_i[i] in numbers:
    exp.append(s_i[i])
  elif s_i[i] in '*+/-':
    while stck: # 스택이 비어있지 않는동안
      top=stck[-1]
      if(top in '*/' and s_i[i] in '+-') or (top in '*/' and s_i[i] in '*/') or (top in '+-' and s_i[i] in '+-'):
        exp.append(stck.pop())
      else:
        break
    stck.append(s_i[i])

while stck: #
  exp.append(stck.pop())
print(''.join(exp))