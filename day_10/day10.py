import sys
import re

def parseLine(cycle,x, line):
    j = re.findall("[-+]?\d+", line)
    if len(j) == 0:
        cycle+=1
        cycles[cycle] = x 
    else: 
        cycles[cycle+1] = x
        cycle += 2 
        x += int(j[0]) 
        cycles[cycle] = x
    return cycle,x
x= 1
cycle = 0
cycles = dict()
cycles[0] = 1
for line in sys.stdin:
    cycle,x = parseLine(cycle,x,line.strip())

def pixel(c,x):
    if x >= c -1 and x <= c+1:
        return '█'
    else:
        return '.' 

total = 0
cp = [220, 180, 140, 100, 60, 20]
for c in cp:
    total += cycles[c-1] * c

print("Part 1:", total)

linex= [['.' for i in range(40)] for j in range(6)]

for c, vals in cycles.items():
    if c != 0:      
        h = (c-1) % 40
        v = int((c-1)/40)
        linex[v][h] = pixel(h, cycles[h+v*40])

for i in range(6):
    linex[i] = "".join(linex[i])

print("Part 2:")
print("\n".join(linex))