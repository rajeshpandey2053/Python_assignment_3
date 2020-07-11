def swapPositions(input_user, pos1, pos2): 
      
    input_user[pos1], input_user[pos2] = input_user[pos2], input_user[pos1] 
    return input_user

# main function
user_input = list()
num = int(input("Enter the number of elements in the list"))
for _ in range(num):
    user_input.append(int(input("Enter item: ")))

#bubble sort
isSorted = False
last_unsorted = num - 1
while(not isSorted):
    isSorted = True
    for i in range(last_unsorted):
        if (user_input[i] > user_input[i+1]):
            swapPositions(user_input,i,i+1)
            isSorted = False
    last_unsorted = last_unsorted - 1


print("Using bubble_sort approach , the sorted output is: ", user_input)