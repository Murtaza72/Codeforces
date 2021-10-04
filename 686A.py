io = input().split()

n = int(io[0])
x = int(io[1])

distress = 0

for i in range(n):
    cmd = input().split()
    if cmd[0] == "-":
        if x - int(cmd[1]) >= 0:
            x -= int(cmd[1])
        else:
            distress += 1
    elif cmd[0] == "+":
        x += int(cmd[1])

print(x, distress)
