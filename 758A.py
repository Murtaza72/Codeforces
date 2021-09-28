n = int(input())

arr = list(map(int, input().split()))
eq = max(arr)
total = 0

for i in range(n):
    if eq - arr[i] != 0:
        total += eq - arr[i]
print(total)
