lr = [1.25, .75]
ud = [1.25, .75]

for i in range(2):
    for j in range(2):
        print((lr[i], ud[j] + 1), end=', ')
        print((-1 * lr[i], ud[j] + 1), end=', ')
        print((lr[i], -1 * ud[j] + 1), end=', ')
        print((-1 * lr[i], -1 * ud[j] + 1), end=', ')