n = int(input())
end = int(n / 2) + 2

for i in range(1, end):
    T = ((i * i) + i) // 2
    if T == n:
        print("YES")
        break
else:
    print("NO")
