# l=['apple','bannana','grape',[0,1,2]]
# if 'apple' in l:
#     print('a')
# else:
#     print('n')

# if 'lemon' not in l:
#     print('nl')

# if 'apple' and 'bannana' or 'berry' in l:
#     print('True')
# else:
#     print('False')
cnt = 0
l2 = [0, 1, 2, 3, 4, 5]
for i in range(len(l2)):
    if l2[i] % 2 == 0 and l2[i] % 3 == 0:
        cnt += 1  # %연산은 a % b = a - (b * (a // b)) 처럼 동작한다
print(cnt)

while 1:
    cnt = 0
    for i in range(5):
        cnt += 1
        print(f"cnt: {cnt}")
    if cnt == 5:
        break
# iterable (반복 가능한 자료형) 안의 요소들을 여러 변수에 "한꺼번에" 할당
print("----------")
l3 = [[0, 1, 2], [1, 3, 4], [6, 5, 6]]
for first, second, third in l3:
    print(first, second, third)
print("----------")
for obj in l3:
    print(obj)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:  # mark에 marks 의 값을 각각 대입
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end="|")
    print()
print("----------")
res = []
for num in marks:
    res = marks.append(num * 2)
print(res)
