arr = list(map(int, input().split()))
arr.sort()

distance = 0
mid = arr[1]

for i in arr:
    distance = distance + abs(i - mid)

print(distance)
