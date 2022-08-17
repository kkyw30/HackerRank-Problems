# goal to perform operation on list based on inputted command

if __name__ == '__main__':
    N = int(input())
    main = [] 
    
    commands = [] 
    for i in range(N):
        commands.append(input())
        
    for command in commands:
        l = command.split()
        if l[0] == 'append':
            main.append(int(l[1]))
        elif l[0] == 'insert':
            main.insert(int(l[1]), int(l[2]))
        elif l[0] == 'remove':
            main.remove(int(l[1]))
        elif l[0] == 'print':
            print(main)
        elif l[0] == 'sort':
            main.sort()
        elif l[0] == 'pop':
            main.pop()
        elif l[0] == 'reverse':
            main.reverse() 