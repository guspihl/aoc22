#Advent of Code 2022 - Day 4

file = open("input.txt", "r")
s1=s2=0
for i in file.read().split('\n'):
    a, b = map(lambda x : map(int, x.split('-')), i.split(','))
    a = list(a);a[1]+=1
    b = list(b);b[1]+=1
    x = set(range(*a))
    y = set(range(*b))

    #Part 1
    if len(x & y) == min(len(x), len(y)):
        s1 += 1
    
    #Part 2    
    if len(x & y)!=0:
        s2 += 1

print("Solution 1", s1)
print("Solution 2", s2)