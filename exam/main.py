"""Bouss Bohdan KV-71"""

import random

n = 10
matrix = [[0 for x in range(n)] for y in range(n)]

# for row in matrix:
#     print(row)

def find_path(posx = 0, posy = 0):
    global n, matrix
    dead_ends = [[0 for x in range(n)] for y in range(n)]
    check = False
    no_way = False
    prevx = 0
    prevy = 0
    if matrix[posx][posy] == 1:
        return False

    while not check:

        matrix[posx][posy] = "X"
        no_way = True
        if matrix[posx + 1][posy] == 0 and posx + 1 < n and posx + 1 >=0 and not posx + 1 == prevx and dead_ends[posx + 1][posy] == 0:
            no_way = False
            prevx = posx
            posx = posx + 1
        if matrix[posx - 1][posy] == 0 and posx - 1 < n and posx - 1 >=0 and not posx - 1 == prevx and dead_ends[posx - 1][posy] == 0:
            no_way = False
            prevx = posx
            posx = posx - 1
        if matrix[posx][posy + 1] == 0 and posy + 1 < n and posy + 1 >=0 and not posy + 1 == prevy and dead_ends[posx][posy + 1] == 0:
            no_way = False
            prevy = posy
            posy = posy + 1
        if matrix[posx][posy - 1] == 0 and posy - 1 < n and posy - 1 >=0 and not posy - 1 == prevy and dead_ends[posx][posy - 1] == 0:
            no_way = False
            prevy = posy
            posy = posy - 1

        if no_way:
            dead_ends[posx][posy] = 1
            matrix[posx][posy] = 0
            x = posx
            y = posy
            posx = prevx
            posy = prevy
            prevx = x
            prevy = y

        if posx == n - 1 and posy == n - 1:
            check = True

    return True


def start():
    if find_path():
        print("conguralation!!!")
        for row in matrix:
            print(row)
    else:
        print("There is no path")

def test(times):
    global matrix, n
    for i in range(times):
        matrix = [[random.randint(0, 1) for x in range(n)] for y in range(n)]
        for row in matrix:
            print(row)
        start()

test(3)
