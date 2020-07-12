#implementing quick sort function
def quick_sort(arr, left, right):
    if (left >= right):
        return
    pivot = arr[(left+right)//2]
    index = partition(arr, left, right, pivot)
    quick_sort(arr, left, index-1)
    quick_sort(arr, index, right) 

#partitioning function
def partition(arr, left, right, pivot):
    while(left<=right):

        while(arr[left]<pivot):
            left = left + 1
        
        while(arr[right] > pivot):
            right = right -1
        
        if (left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left = left + 1
            right = right -1
        
    return left

# main function
arr = list()
num = int(input("Enter the number of elements in the list"))
for _ in range(num):
    arr.append(int(input("Enter item: ")))
quick_sort(arr,0,num-1)
print("The sorted array using quick sort is: ",arr)