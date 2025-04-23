lst=[]
n=int(input('input n: '))
for i in range(n):
  if i%3==0 and i%2!=0:
    lst.append(i)
print(lst)