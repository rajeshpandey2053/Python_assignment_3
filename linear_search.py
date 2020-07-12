def linear_search(array, find_num):
    for i in range(len(array)-1):
        if array[i] == find_num:
            return i
    
    return -1

arr = [1,2,3,4,8,9]
num = int(input("Enter the number you want to search: "))
a = linear_search(arr, num)
if (a == -1):
    print("not foiund")
else: 
    print("Found!! The index is: ", a+1)
