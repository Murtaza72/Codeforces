io = input().split()
n = int(io[0])
c = int(io[1])

scores = list(map(int, input().split()))
times = list(map(int, input().split()))


def limak(scores, times):
    points = 0
    curr_time = times[0]

    for i in range(n):
        points += max(0, scores[i] - (c * curr_time))
        if len(times) > i + 1:
            curr_time += times[i + 1]
        else:
            break

    return points


def radewoosh(scores, times):
    points = 0
    curr_time = times[-1]

    for i in range(n - 1, -1, -1):
        points += max(0, scores[i] - (c * curr_time))
        if i - 1 >= 0:
            curr_time += times[i - 1]
        else:
            break

    return points


# print(limak(scores, times))
# print(radewoosh(scores, times))

if limak(scores, times) > radewoosh(scores, times):
    print("Limak")
elif limak(scores, times) < radewoosh(scores, times):
    print("Radewoosh")
else:
    print("Tie")
