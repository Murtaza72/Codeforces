io = input().split()

n = int(io[0])
m = int(io[1])

on = [False] * m

for i in range(n):
    buttons = list(map(int, input().split()))
    buttons.pop(0)
    for j in range(1, m + 1):
        if j in buttons:
            on[j - 1] = True

if all(on):
    print("YES")
else:
    print("NO")
