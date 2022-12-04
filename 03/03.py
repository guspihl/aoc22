#Advent of Code 2022 - Day 3

file = open("input.txt", "r")
a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

s1 = s2 = 0
l = []

for i in file.read().split('\n'):
    l.append(i)

    #Part 1
    fh, lh = set(i[:len(i)//2]), set(i[len(i)//2:]) 
    s1 += a.index((fh & lh).pop())+1

    #Part 2
    if len(l) == 3:
        x,y,z = map(set, l)
        s2 += a.index((x & y & z).pop())+1
        l.clear()

print("Solution 1:", s1)
print("Solution 2:", s2)
