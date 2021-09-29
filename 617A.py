n = int(input())

steps = 0

while n > 0:
    if n - 5 >= 0:
        n -= 5
        steps += 1
        # print(n)
    elif n - 4 >= 0:
        n -= 4
        steps += 1
        # print(n)
    elif n - 3 >= 0:
        n -= 3
        # print(n)
        steps += 1
    elif n - 2 >= 0:
        n -= 2
        # print(n)
        steps += 1
    elif n - 1 >= 0:
        n -= 1
        steps += 1
        # print(n)

print(steps)
