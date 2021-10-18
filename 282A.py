n = int(input())

x = 0

for i in range(n):
    oprt = input()
    if "++" in oprt:
        x += 1
    else:
        x -= 1

print(x)
    