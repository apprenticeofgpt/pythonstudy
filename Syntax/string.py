str1="I ate % apples" % "Five" # string formatting
print(str1) 

a="20250312rainy"
date=a[0:8]
weather=a[8:]
print(date,weather,end=".")
print()

l=[1,2,3,4,5] #list
str2="I ate %d cookies and %d cups of milk" %(l[3],l[0])
print(str2)

lol="lol"
str3=r"in %s you can put anything  "+"%s" %lol
print(str3)

# 전체 길이가 10개인 문자열 공간에서 오른쪽 정렬
print("%10s"%"hi") 
# 전체 길이가 10개인 문자열 공간에서 왼쪽 정렬
print("%-10s"%"hi") 

print("%0.5f"%3.141592) # 소수점 10자리까지 표현

number=3
number2=4
print("I ate {0} cookies".format(number))#formate 함수를 사용한 포매팅
print("I ate{0} cookies and {1} cups of milk".format(number,number2))

print("{0:<10}".format("Hello")) # 치환 되는 문자열 왼쪽으로 정렬
print("{0:>10}".format("Hi"))
print("{0:=^6}".format("hey")) # 치환 되는 문자열 가운데 정렬

# f문자열 포팅
# 문자열 앞에 f접두사를 붙이면 f문자열 포팅 사용 가능
name="greg";backnum=31;age=25
print(f'{name} maddux back number is {backnum}')
d={'name':'greg','age':25}
print(f'My name is {d["name"]} and I am {d["age"]} years old')

print(f'{"Hi:<10"}')
print(f'{"Hello":=^10}')

print(name.find('g')) # 문자열에서 특정 문자의 위치를 찾는 함수
print(name.find('x')) # 없는 문자를 찾으면 -1을 반환    
print(name.index('g')) # find와 비슷하지만 없는 문자를 찾으면 오류를 발생시킴  

stringlist=['a','b','c','d','e'] #join함수는 리스트의 요소를 문자열로 연결
print(",".join(stringlist[0:]))
print((stringlist[0:]))
print(name.upper()) # 대문자로 변환
print(name.lower()) # 소문자로 변환

print(name.replace('g','G'))
