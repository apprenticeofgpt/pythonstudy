
import tkinter as tk
import random
"""
| 위젯       | 설명       | 예시                                       |
| -------- | -------- | ---------------------------------------- |
| `Label`  | 글자 표시    | `tk.Label(root, text="안녕")`              |
| `Button` | 버튼       | `tk.Button(root, text="클릭", command=함수)` |
| `Entry`  | 한 줄 입력창  | `tk.Entry(root)`                         |
| `Text`   | 여러 줄 입력창 | `tk.Text(root)`                          |
| `Frame`  | 위젯 그룹화   | `tk.Frame(root)`                         |
| `Canvas` | 그림 그리기   | `tk.Canvas(root, width=300, height=200)` |
| 방법                     | 설명                    |
| ---------------------- | --------------------- |
| `.pack()`              | 위에서 아래로 자동 배치 (가장 간단) |
| `.grid(row=, column=)` | 행렬 배치 (폼 만들 때 유용)     |
| `.place(x=, y=)`       | 픽셀 위치 지정 (정밀 배치)      |

"""
root=tk.Tk()

label=tk.Label(root,text='hello')
label.pack()

root.geometry('300x300')

root.mainloop()