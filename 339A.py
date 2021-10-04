s = list(map(int, input().split("+")))
s.sort()
print("+".join(str(i) for i in s))
