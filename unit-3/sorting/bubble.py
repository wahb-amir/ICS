def compare(a, b, mode):
    if mode == "ascending":
        return a > b
    elif mode == "descending":
        return a < b
    raise ValueError("mode must be 'ascending' or 'descending'")


def bubble_sort(arr: list, mode: str = "ascending") -> list:
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if compare(arr[j], arr[j + 1], mode):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            print(f"sorting took {i+1} passes!" if i > 0 else "list is already sorted!")
            break
    return arr
                
            
        

li = [9,12,3,1,8]
s = [1, 3, 8, 9, 12]

sorted = bubble_sort(s, "ascending")
print(sorted)
sorted = bubble_sort(li, "ascending")
print(sorted)