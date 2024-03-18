N = int(input())

darray = []

for _ in range(N):
    command = input().split()

    if command[0] == 'push_back':
        darray.append(int(command[1]))
    elif command[0] == 'pop_back':
        if darray:      
            darray.pop()
    elif command[0] == 'size':
        print(len(darray))
    elif command[0] == "get":
        k = int(command[1])
        if k <= len(darray):
            print(darray[k-1])