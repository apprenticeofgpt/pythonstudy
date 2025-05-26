def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  
lst=[i for i in range(10)]
print(lst)

print(linear_search(lst,5))
