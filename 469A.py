max_level = int(input()) 

X = list(map(int, input().split()))[1:]
Y = list(map(int, input().split()))[1:]

levels = list(set(X+Y))

all_level = [0] * max_level

for i in range(max_level):
    if i+1 in levels:
        all_level[i] = 1
  
if all(all_level):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
     