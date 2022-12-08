#Advent of Code 2022 - Day 8

from numpy import array as arr
from itertools import takewhile as tw

lines = open("input.txt", "r").read().split('\n')

grid = arr([[int(y) for y in x] for x in lines])

c = len(grid)*4-4
b = []

for i in range(1, len(grid)-1):
    for j in range(1, len(grid)-1):
        pos = grid[i][j]

        u = grid[0:i, j][::-1]
        d = grid[i+1:, j]
        l = grid[i][0:j][::-1]
        r = grid[i][j+1:]

        #Part 1
        c += any([pos > x for x in [max(u), max(d), max(l), max(r)]])

        #Part 2
        ul = len(list(tw(lambda x : x < pos, u)))
        dl = len(list(tw(lambda x : x < pos, d)))
        ll = len(list(tw(lambda x : x < pos, l)))
        rl = len(list(tw(lambda x : x < pos, r)))

        if ul != len(u): ul+=1
        if dl != len(d): dl+=1
        if ll != len(l): ll+=1
        if rl != len(r): rl+=1
        
        b.append(ul * dl * ll * rl)

print("Solution 1:", c)
print("Solution 2:", max(b))