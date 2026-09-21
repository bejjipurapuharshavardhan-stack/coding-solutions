N = int(input())
stamps = set()

for _ in range(N):
    country = input().strip()
    stamps.add(country)

print(len(stamps))
