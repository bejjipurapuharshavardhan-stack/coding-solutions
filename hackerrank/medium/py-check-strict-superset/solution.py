set_A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    current_set = set(map(int, input().split()))
    
    if not (set_A.issuperset(current_set) and set_A != current_set):
        is_strict_superset = False
        break

print(is_strict_superset)
