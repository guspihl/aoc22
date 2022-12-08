#Advent of Code 2022 - Day 7

lines = open("input.txt", "r").read().split('\n')

d = {}
for i in lines:
    match i.split():
        case '$', 'cd', '/': path = ['/']   
        case '$', 'cd', '..': path.pop()
        case '$', 'cd', cd: path.append(path[-1]+'/'+cd)
        case '$', 'ls': pass
        case 'dir', folder: pass
        case size, file:
            for x in path:
                if x in d:
                    d[x] += int(size)
                else:
                    d[x] = int(size)
    print(path)

print("Solution 1:", sum([x for x in d.values() if x <= 100000]))
print("Solution 2:", min([x for x in d.values() if x >= 30000000-(70000000-d['/'])]))