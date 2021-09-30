s = list(input())

flip = 0

for i in s:
    if i.isdigit():
        if int(i) % 2 != 0:
            flip += 1
    elif i in ["a", "e", "i", "o", "u"]:
        flip += 1

print(flip)
