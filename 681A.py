n = int(input())

good = 0

for i in range(n):
    info = input().split()
    before = int(info[1])
    after = int(info[2])
    if before >= 2400 and after > before:
        good += 1

if good > 0:
    print("YES")
else:
    print("NO")
