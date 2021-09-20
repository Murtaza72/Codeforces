io = input().split()
n = int(io[0])
m = int(io[1])

chips_left = m
l = []
i = 1

while chips_left >= 0:
        chips_left -= i
        l.append(chips_left)
        i += 1
        i = i % (n+1)
print(l[-2])