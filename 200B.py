n = int(input())

milli = list(map(int, input().split()))
total = 0

for i in milli:
    total += i
    
print("%.15f" % (total/len(milli)))