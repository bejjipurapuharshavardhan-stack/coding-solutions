num_student1 = int(input())
set1 = set(map(int, input().split()))
num_student2 = int(input())
set2 = set(map(int, input().split()))

res = set1.union(set2)
print(len(res))

