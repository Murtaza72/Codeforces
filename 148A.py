k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damage = 0

for i in range(1, d+1):
    if i % k == 0:
        damage += 1
    elif i % l == 0:
        damage += 1
    elif i % m == 0:
        damage += 1
    elif i % n == 0:
        damage += 1
        
print(damage)