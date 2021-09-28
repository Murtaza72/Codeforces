num1 = input()
num2 = input()

for i in range(len(num1)):
    if num1[i] != num2[i]:
        print("1", end='')
    else:
        print("0", end='')
