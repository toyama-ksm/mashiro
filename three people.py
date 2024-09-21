n = int(input())
count = 0
for i in range(0,n):
    votes = list(map(int, input().split()))
    if sum(votes) >= 2:
        count += 1

print(count)
