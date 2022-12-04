#Advent of Code 2022 - Day 2

file = open("input.txt", "r")

x=1
y=2
z=3

d1 = {
    'A': {'X': 3+x, 'Y': 6+y, 'Z': 0+z},
    'B': {'Y': 3+y, 'Z': 6+z, 'X': 0+x},
    'C': {'Z': 3+z, 'X': 6+x, 'Y': 0+y}
    }

a = 0
b = 3
c = 6

d2 = {
    'A': {'X': 3+a, 'Y': 1+b, 'Z': 2+c},
    'B': {'Y': 2+b, 'Z': 3+c, 'X': 1+a},
    'C': {'Z': 1+c, 'X': 2+a, 'Y': 3+b}
    }

s1 = s2 = 0

for i in file.read().split('\n'):
    o, m = i.split()
    s1 += d1[o][m]
    s2 += d2[o][m]

print("Solution 1:", s1)
print("Solution 2:", s2)