def bubble_sort(arr:list)->list:
    lenght = len(arr)
    for i in range(lenght):
        swapped = False
        for j in range(lenght-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped:
            print(f"sorting took {i+1} passes!" if i > 0 else "list is already sorted!")
            break
    return arr
                
            
        

li = [9,12,3,1,8]
s = [1, 3, 8, 9, 12]

sorted = bubble_sort(s)
print(sorted)
sorted = bubble_sort(li)
print(sorted)