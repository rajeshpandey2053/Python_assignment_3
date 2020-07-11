# main function
user_input = list()
num = int(input("Enter the number of elements in the list"))
for _ in range(num):
    user_input.append(int(input("Enter item: ")))

# insertion sort
for i in range(1,6):
    value = user_input[i]
    space = i

    while(space > 0 and user_input[space - 1] > value):
        user_input[space] = user_input[space - 1]
        space = space - 1

    user_input[space] = value

print(user_input)

    
