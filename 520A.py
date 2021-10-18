input()

word = input().lower()
container = {'a': False,'b': False,'c': False,'d': False,'e': False,'f': False,'g': False,'h': False,'i': False,'j': 0,'k': False,'l': False,'m': False,'n': False,'o': False,'p': False,'q': False,'r': False,'s': False,'t': 0,'u': False,'v': False,'w': False,'x': False,'y': False,'z': False}

for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in word:
        container[i] = True

if all(container.values()):
    print("YES")
else:
    print("NO")