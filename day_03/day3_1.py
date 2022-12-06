import sys

def check(sac1, sac2):
    common = []
    for c in sac1:
        if c in sac2 and c not in common:
            common.append(c)
    return common

def asignValue(c):
    charValue = ord(c)
    if(charValue > 96):
        return charValue - 96
    else:
        return charValue - 64 + 26

sumOfPriorities = 0
for line in sys.stdin:
    numItems = int(len(line.replace("\n","")) /2) 
    sac1 = line[0:(numItems)]
    sac2 = line[numItems:]
    commonx = check(sac1, sac2)
    for c in commonx:
        sumOfPriorities += asignValue(c)

print("sumOfPriorities = ", sumOfPriorities)