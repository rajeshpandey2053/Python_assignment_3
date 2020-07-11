def merge(left, right, arr):
    i = 0
    j =0 
    k = 0
    while ( i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    
    # if remaining in left

    while(i < len(left)):
        arr[k] = left[i]
        i = i +1
        k = k + 1

# if remaining in right
    while(i < len(right)):
        arr[k] = right[i]
        i = i +1
        k = k + 1
    
  


def merge_sort(arr):
    if len(arr)<2:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right,arr)

#main function
arr = list()
num = int(input("Enter the number of elements in the list"))
for _ in range(num):
    arr.append(int(input("Enter item: ")))

    
merge_sort(arr)
print("The sorted list through merge sort is : ", arr)