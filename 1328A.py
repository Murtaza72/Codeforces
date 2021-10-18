n = int(input())

for _ in range(n):
    io = input().split()
    a = int(io[0])
    b = int(io[1])
    
    if a % b == 0:
        print(0)
    else:
        print(b - a % b) 
        
# tried by checking if a % b is true 
# and if false: a += 1
# but that takes loooong time for huuuuge numbers
# so used this formula
# found in the tutorial sectio