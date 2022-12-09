import sys

def process(heigth, lines):
    visible = False
    score = 1
    for l in lines:
        for i, t in enumerate(l,1):
            if t >= heigth:
                score *= i
                break
        else: #For... else staments
            score *=  len(l) # this takes care of the borders. 
            visible = True # if no other tree is higher in the line, then this tree must be visible
    return visible, score

visibleTrees = maxScore = 0
forest = []
for x,y in enumerate(sys.stdin):
    forest.append( list(int(c) for c in y.strip())) #List comprehension

for x, z in enumerate(forest):
    for y,height in enumerate(z): 
        ltrees = z[0:y][::-1] # [::-1] to reverse a list!
        rtrees = z[y+1:]
        utrees = [t[y] for t in forest[0:x][::-1]]
        dtrees = [t[y] for t in forest[x+1:]]
        lines = [ltrees, rtrees,utrees,dtrees]
        visible, score = process(height, lines)
        visibleTrees += int(visible)
        maxScore = max(maxScore, score)

print("Part 1:", visibleTrees)
print("Part 2:", maxScore)