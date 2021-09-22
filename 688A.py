io = input().split()

n = int(io[0])
d = int(io[1])

beat = 0
ans = 0

for i in range(d):
    s = input()

    if s == "1" * n:
        beat = 0
    else:
        beat += 1

    ans = max(ans, beat)

print(max(ans, beat))
