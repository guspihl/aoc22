#Advent of Code 2022 - Day 5
from copy import deepcopy
 
file = open("input.txt", "r")
prep, l = map(lambda x : x.split('\n'), file.read().split('\n\n'))
stacks = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
key = prep[-1]
for i in reversed(prep[:-1]):
    for j,x in enumerate(i):
        if x.isalpha():
            stacks[key[j]].append(x)
 
stacks_2 = deepcopy(stacks)
 
for i in l:
    _, n, _, f, _, t = i.split()
    n = int(n)
    #Part 1
    for j in range(n):
        stacks[t].append(stacks[f].pop())
 
    #Part 2
    for j in stacks_2[f][-n:]:
        stacks_2[t].append(j)
    stacks_2[f] = stacks_2[f][:-n]
 
print("Solution 1:", "".join([x[-1] for x in stacks.values()]))
print("Solution 1:", "".join([x[-1] for x in stacks_2.values()]))