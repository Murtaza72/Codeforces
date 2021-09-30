n = int(input())

shape = {
    "tetrahedron": 4,
    "cube": 6,
    "octahedron": 8,
    "dodecahedron": 12,
    "icosahedron": 20,
}

face = 0

for i in range(n):
    s = input()
    if s.lower() in shape:
        face += shape[s.lower()]

print(face)
