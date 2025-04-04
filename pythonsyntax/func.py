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
"""
lambda 함수
익명 함수, 한줄로 쓰는 함수,return 을 사용하지 않아도 표현식의 결과를 자동으로 반환
lambda 매개변수들: 표현식
ex) lambda x,y:x+y
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
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
while len(primes) < 5:
    n = int(input("input number: "))
    if is_prime(n):
        primes.append(n)

print("입력한 소수들:", primes)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_filter = filter(lambda x: x % 2 == 0, l)
print(list(even_filter))
lamb_map = map(lambda x: x**2, l)
print(list(lamb_map))
filter_map = map(lambda x: x**2, filter(lambda x: x % 2 == 0, l))
print(list(filter_map))
l.reverse()
print(l)
l.sort()
print(l)
students = [("철수", 82), ("영희", 91), ("민수", 75), ("수진", 89)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

print("prime numbers", l)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 10
print(f"The factorial of {n} is{factorial(n)}")
