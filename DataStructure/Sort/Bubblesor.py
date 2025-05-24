#bubble
import random as r
def bubble_sort(arr):
  n=len(arr)
  for i in range(n-1):
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]

lst=[r.randint(0,10) for i in range(10)]
print(lst)
bubble_sort(lst)
print(lst)
