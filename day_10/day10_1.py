import sys
import re

cycles = dict()

def parseLine(cycle,x, line):
    #print(line)
    j = re.findall("[-+]?\d+", line)
    if len(j) == 0:
        #x+=1
        cycle+=1
        cycles[cycle] = x 
    else: 
        #return int(j[0]) 
        cycles[cycle+1] = x
        cycle += 2
        
        x += int(j[0]) 
        cycles[cycle] = x
        #print(3 + int(j[0]) )
    #return x, i
    return cycle,x
x= 1
cycle = 1
cycles[1] = 1
for line in sys.stdin:
    cycle,x = parseLine(cycle,x,line.strip())

#print(cycle,x)
#print(cycles)
c = 220
total = 0
cp = [220, 180, 140, 100, 60, 20]
for c in cp:
    total += cycles[c] * c
print(total)