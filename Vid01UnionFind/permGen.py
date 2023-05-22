lr = [1.25, .75]
ud = [1.25, .75]

for i in range(2):
    for j in range(2):
        print((lr[i], ud[j]), end=', ')
        print((-1 * lr[i], ud[j]), end=', ')
        print((lr[i], -1 * ud[j]), end=', ')
        print((-1 * lr[i], -1 * ud[j]), end=', ')