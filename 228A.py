shoes = list(map(int, input().split()))

have = []

for i in shoes:
    if i not in have:
        have.append(i)
        
print(4 - len(have))