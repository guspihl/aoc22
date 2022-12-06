#Advent of Code 2022 - Day 6

file = open("input.txt", "r").read()

def sol(n):
    for i in range(n, len(file)):
        if len(set(file[i-n:i])) == n:
            return i
 
print("Solution 1:", sol(4))
print("Solution 2:", sol(14))