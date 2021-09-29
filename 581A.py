io = input().split()
a = int(io[0])
b = int(io[1])

diff = same = 0

for i in range(max(a, b)):
    if (a > 0) and (b > 0):
        diff += 1
        a -= 1
        b -= 1
    elif a >= 2:
        same += 1
        a -= 2
    elif b >= 2:
        same += 1
        b -= 2

print(diff, same)
