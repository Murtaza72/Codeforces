io = input().split()
n = int(io[0])
m = int(io[1])

awake = 0


for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(0, 2 * m, 2):  # skipping on 2 because 2 windows in a room
        if (arr[j] == 1) or (arr[j + 1] == 1):  # checking if either window is on
            awake += 1

print(awake)
