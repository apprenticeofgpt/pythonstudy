"""
파이썬 함수의 구조
def 함수이름(매개변수):
    수행할 내용
    return
"""

"""
- def func(num=1)
    디폴트 매개변수
    인자값을 전달해 주지 않으면 기본값이 사용
- def func(*args)
    가변 위치 매개변수
    여러 개의 인수를 튜플로 받음
- def greet(name, *, age)
    *이후에 오는 매개변수는 반드시 키워드로만 전달달
- def func(**kwargs)
    여러 개으 키워드 인수를 딕셔너리로 받음
-   함수의 리턴값은 언제나 하나다다
"""


def addmany(*args):
    res = 0
    for i in args:
        res = res + i
    return res


for i in range(1, 10):
    print(addmany(i), end=" ")


def AddOrMul(char, *args):
    res = 0
    if char == "+":
        for i in args:
            res += i
    elif char == "*":
        res *= i
    return res


def print_kwargs(**kwargs):
    print(kwargs)


print()
print(AddOrMul("+", 1, 2, 3, 4, 5))
print_kwargs(a=1, b=2, c=3, d=[1, 2])

# 소수를 5번 입력받으면 종료하고 소수를 출력
def prime(num):
    if num < 2:
        return False
    isPrime = True
    for i in range(2, int(num**0.5) + 1):
        if n % i == 0:
            isPrime = False
            break

    if isPrime == True:
        l[l_index] = num
        l_index += 1
    return 
l = [None] * 5
l_index = 0
while l_index < 5:
    n = int(input("input number: "))

print("prime numbers", l)
