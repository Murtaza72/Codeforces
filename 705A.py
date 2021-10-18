n = int(input())

feelings = ""

for i in range(1,n+1):
    if i % 2 == 0:
        feelings += "I love that "
    else:
        feelings += "I hate that "

feelings.strip()
feelings = feelings[:-6] + " it"  # slice until "that" 
print(feelings)