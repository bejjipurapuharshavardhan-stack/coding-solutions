for _ in range(int(input())):
    a_len = int(input())
    set1 = set(map(int, input().split()))
    b_len = int(input())
    set2 = set(map(int, input().split()))
    print(set1.issubset(set2))
    
