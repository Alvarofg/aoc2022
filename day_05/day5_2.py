import sys
import re

def parseIntructions(stacks, instruction):
    #move 1 from 2 to 1
    x = re.findall("\d+", instruction)
    num = int(x[0])
    source = int(x[1])-1
    dest = int(x[2])-1
    move = stacks[source][-num:]
    stacks[source] =  stacks[source][0:-num:]
    stacks[dest].extend(move) 

a = list(map(str, sys.stdin))
b = "".join(a).split("\n\n")
setup = b[0]
instructions = b[1].split("\n")
c = setup.split("\n")
numStacks = int(c.pop().split("  ").pop())
maxLen = len(c)
emptyStack =  [None for i in range(maxLen)]  
stacks = [list(emptyStack) for i in range(numStacks)] 
while len(c) >= 1:
    cp = c.pop()
    levelIndex =  maxLen - len(c) -1
    for x in range(1,numStacks+1 ):
        crate = (cp[(x*4)-3])
        stackNumber = x-1
        stacks[stackNumber][levelIndex] = str(crate)

stacks= list(map(lambda x: list(filter(lambda x: x != ' ',x)),stacks))

instructions.pop()
for intruction in instructions:
    parseIntructions(stacks, intruction)

t = list(map(lambda x : x[-1], stacks))
print("".join(t))