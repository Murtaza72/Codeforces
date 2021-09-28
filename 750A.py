io = input().split()
n = int(io[0])
k = int(io[1])

solved = 0

min_left = 240 - k

for i in range(1, n + 1):
    min_left = min_left - (5 * i)
    if min_left >= 0:
        solved += 1
print(solved)
