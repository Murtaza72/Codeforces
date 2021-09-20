n = int(input())

solution = []

for _ in range(n):
    solution.append(list(map(int, input().split())))

win = 0

for i in solution:
    if i.count(1) >= 2:
        win += 1

print(win)