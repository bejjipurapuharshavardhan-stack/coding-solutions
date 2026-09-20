m = int(input())
elements_a = input().split() 

my_set1 = set()
count = 0 

while count < m:
    item = int(elements_a[count])
    my_set1.add(item)
    count += 1

n = int(input())
elements_b = input().split()

my_set2 = set()
count = 0

while count < n:
    item = int(elements_b[count])
    my_set2.add(item)
    count += 1

result = my_set1.symmetric_difference(my_set2)

for num in sorted(result):
    print(num)
    



