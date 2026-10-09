def sort(arr):
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
        
    return arr

li = [9,12,3,1,8]
sorted = sort(li)
print(sorted)