import sys
import re

def printSprint(c):
    return
    sprite = ["."]*40
    sprite[c-1] = sprite[c] = sprite[c+1] = "#"
    # print("S:","".join(sprite))

def printPx(c):
    return
    sprite = ["."]*40
    sprite[c] = "X"
    # print("P:", "".join(sprite))

def printLx(l):
    return
    print("O:", "".join(l))

def pixel(c,x):
    if x >= c -1 and x <= c+1:
        return '#'
    else:
        return '.' 

def parseLine(cycle,x, line, linex):
    px = (cycle-1) % 40
    # print(px)
    j = re.findall("[-+]?\d+", line)
    if len(j) == 0: #noop
        linex += pixel(px, x)
        cycle += 1
        px += 1
        cycles[cycle] = x 

    else: #addx
        printPx(px)
        printSprint(x)
        linex += pixel(px, x)
        printLx(linex)
        cycle += 1
        px += 1
        printPx(px)
        printSprint(x)
        linex += pixel(px, x)
        printLx(linex)
        cycle += 1
        px += 1       
        cycles[cycle] = x
        x += int(j[0]) 
        cycles[cycle] = x
    return cycle,x
x= 1
cycle = 1
cycles = dict()
linex = []
cycles[1] = 1
for line in sys.stdin:
    cycle,x = parseLine(cycle,x,line.strip(), linex)

# screenLines = ["."*40]*int(6)

print("".join(linex[0:39]))
print("".join(linex[40:80]))
print("".join(linex[80:120]))
print("".join(linex[120:160]))
print("".join(linex[160:200]))
print("".join(linex[200:240]))

# line = ''
# for c,x in cycles.items():
#     # print(c, x, pixel(c,x))
#     line += pixel(c,x)
#     # print(c)
    # if(c > 20):
    #     break

# print("".join(line[0:40]))
# print("".join(line[41:81]))
# 
# print(line)
#print(cycle,x)
#print(cycles)
# c = 220
# total = 0
# cp = [220, 180, 140, 100, 60, 20]
# for c in cp:
#     total += cycles[c] * c
#print(total)

# #print(cycles)
# # for c in cycles:
# #     print(c-1)
# print( int(50 / 40))
# print(50 % 40)

# h = len(cycles) / 40
# print(h)
# screenLines = ["."*40]*int(h)

# tmp = list(screenLines[0])
# tmp[1] = "#"
# screenLines[1] = "".join(tmp)  
# #screenLines[1][1]= '#'
# #for 
# # for s in tailsets[8]:
# #     x, y = s
# #     # print(x, y) 
# #     tmp = list(chart[y])
# #     tmp[x] = "#"
# #     chart[y] =  "".join(tmp)

# # tmp = list(chart[0])
# # tmp[0] = "s"
# # chart[0] =  "".join(tmp)

# print("\n".join(screenLines))
# #print("\n".join(screenLines[::-1]))