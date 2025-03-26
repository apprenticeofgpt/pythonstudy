d={1:'a'}
d[2]='b' # 딕셔너리 값 추가
print(d)
d['name']='greg'
d[3]=[1,2,3]
print(d)
del d[1] # 키가 1인 값과 쌍 삭제
print(d)

"""
>>> a = {[1,2] : 'hi'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
딕셔너리에서 키값으로 리스트를 사용할 수 없음

"""
print(d.keys()) #키 값들을 나열
print(d.values()) #값들을 나열
print(d.items()) #키와 값 쌍을 나열
"""
d.clear()
딕셔너리 안의 모든 요소를 삭제
"""
