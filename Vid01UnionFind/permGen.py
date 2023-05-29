import random
numPoints = 30
def shouldConnect(p):
    return random.random() < p

maxPos = 3 
minPos = -3

s = set()
d = {}

vertices = [i for i in range(1, numPoints + 1)]
edges = []
for i in range(1, len(vertices) + 1):
    for j in range(i + 4, len(vertices) + 1):
        if shouldConnect(.10):
            edges.append((i, j))

def bad(t):
    return t in s

for i in range(1, len(vertices) + 1):
    pos = [random.randint(minPos - 2, maxPos + 2), random.randint(minPos, maxPos), 0] 
    while bad(str(pos)):
        pos = [random.randint(minPos - 2, maxPos + 2), random.randint(minPos, maxPos), 0] 
    s.add(str(pos))
    d[i] = pos

print(edges)

        
