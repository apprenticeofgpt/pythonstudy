import random as r
frames=[] 
score=[0]*10
bonus_score=[]
total=0
for i in range(10):
  first=r.randint(0,10)
  second=r.randint(0,10-first)
  frames.append([first,second])
print(frames)
for i in range(10):
  first, second = frames[i]
  #strike
  if first==10:
    score[i]=10+frames[i+1][0]+frames[i+1][1]
  #spare
  elif first+second==10:
   score[i]=10+frames[i+1][0]
  else:
    score[i]=first+second
print(score)
