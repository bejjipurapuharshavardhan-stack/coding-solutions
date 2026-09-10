if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command_data = input().split()
        action = command_data[0]
        
        if action == "insert":
            index = int(command_data[1])
            number = int(command_data[2])
            my_list.insert(index, number)
        elif action == "print":
            print(my_list)
        elif action == "remove":
            number = int(command_data[1])
            my_list.remove(number)
        elif action == "append":
            number = int(command_data[1])
            my_list.append(number)
        elif action == "sort":
            my_list.sort()
        elif action == "pop":
            my_list.pop()
        elif action == "reverse":
            my_list.reverse()
