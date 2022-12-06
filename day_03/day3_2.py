import sys
# Run as cat .\input.txt | python .\day3_2.py 
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

def groupCheck(group):
    common12 = check(group[0], group[1])
    common123 = check(common12, group[2])
    return asignValue(common123[0])

sumOfPriorities = 0
group = []
i=0
for line in sys.stdin:
    if i<3:
        group.append(line.replace("\n",""))
        i += 1
    else:
        i=1
        sumOfPriorities += groupCheck(group)
        group.clear()
        group.append(line.replace("\n",""))

sumOfPriorities += groupCheck(group)
print("sumOfPriorities = ", sumOfPriorities)

