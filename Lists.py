# we create a list and perform all the 7 commands according to the inputs.
# For this we read N the no. of commands
# In the range of commands we perform the action.
N = int(input())
L = []

for i in range(N):
    command = input().split()
    #print command
    if command[0] == 'insert':
        L.insert(int(command[1]), int(command[2]))
    elif command[0] == 'append':
        L.append(int(command[1]))
    elif command[0] == 'remove':
        L.remove(int(command[1]))
    elif command[0] == 'pop':
        L.pop()
    elif command[0] == 'sort':
        L.sort()
    elif command[0] == 'reverse':
        L.reverse()
    elif command[0] == 'index':
        print(L.index(command[1]))
    elif command[0] == 'count':
        print(L.count(command[1]))
    else:
        print(L)
