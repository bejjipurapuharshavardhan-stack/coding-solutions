num_elements_A = int(input())
set_A = set(map(int, input().split()))
num_N = int(input())

for _ in range(num_N):
    command_line = input().split()
    command = command_line[0]
    
    other_set = set(map(int, input().split()))
    
    if command == "update":
        set_A.update(other_set)
    elif command == "intersection_update":
        set_A.intersection_update(other_set)
    elif command == "difference_update":
        set_A.difference_update(other_set)
    elif command == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
        
print(sum(set_A))
