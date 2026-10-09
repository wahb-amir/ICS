def search(arr,target):
    left = 0
    right = len(arr)-1
    mid = right // 2
    for _ in range(len(arr)):
        if target == arr[mid]:
            return mid
        elif arr[mid] > target:
            left = mid
            mid = (left + right)//2
        else:
            right = mid
            mid = (left+right)//2
    return None


li = [12, 9, 8, 3, 1]


result = search(li,3)

print(result)