def binary_search(arr, find_num):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = (start + end)//2
        if arr[mid] == find_num:
            return mid
        elif find_num<arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [1,2,3,4,8,9]
num = int(input("Enter the number you want to search: "))
a = binary_search(arr, num)
if (a == -1):
    print("not foiund")
else: 
    print("Found!! The index is: ", a+1)
