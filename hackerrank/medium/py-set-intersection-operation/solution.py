student_num1 = int(input())
set1 = set(map(int, input().split()))
student_num2 = int(input())
set2 = set(map(int, input().split()))

res = set1.intersection(set2)
print(len(res))
