l=[1,2,3,4,5] #list
s={1,2,3,4,5} #set
d={1:1,2:2,3:3,4:4,5:5} #dictionary
t=(1,2,"hello",[4,5]) #tuple

print(l[0:5])
l[0:5]=[10,20,30,40,50]
print(l[0:5])
print(t[0:3])
print(l[-5])
t[3][0]=1000
print(t[0:4])

for index,value in enumerate(l):
    print(index,value)

s = 'First line.\nSecond line.'  # \n means newline
print(s)
print(3 * 'un' + 'ium')

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b