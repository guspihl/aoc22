#Advent of Code 2022 - Day 1

file = open("input.txt", "r")
l = []

for i in file.read().split('\n\n'):
    l.append(sum([int(x) for x in i.split('\n')]))

print("Solution 1:", max(l))
print("Solution 2:", sum(sorted(l)[::-1][:3]))