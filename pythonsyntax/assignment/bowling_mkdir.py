import random as r
import os
"""
N명의 사람
볼링 기록 저장
파일을 여는 함수
"""
n_ppl = int(input())
names = {}
for _ in range(n_ppl):
    name = input("name: ")
    frames = []
    for _ in range(10):
        first = r.randint(0, 10)
        second = r.randint(0, 10 - first)
        frames.append([first, second])
    names[name] = frames
