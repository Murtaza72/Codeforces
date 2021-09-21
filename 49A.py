ques = input().lower().strip("?").split()

if ques[-1][-1] in [
    "a",
    "e",
    "i",
    "o",
    "u",
    "y",
]:
    print("YES")

else:
    print("NO")
