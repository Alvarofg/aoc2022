import sys

forest = dict()

def isBorder(x, y, forest):
    border = len(forest) -1 
    
    if x== 0 or y == 0:
        return 1    
    elif x == border or y == border:
        return 1
    else:
        return 0

def compareViz(x, y, forest):
    tree = forest[x][y]
    border = len(forest)
    tallestleft = tallestright = tallestup = tallestdown =True
    
    right = left = up = down = ''
    for c in range(y+1, border):
        tallestright =  tallestright and tree > forest[x][c]
        right +=  forest[x][c]
    
    for c in range(0,y):
        tallestleft = tallestleft and tree > forest[x][c] 
        left +=  forest[x][c]
    
    for c in range(x+1, border):
        tallestdown = tallestdown and tree > forest[c][y] 
        down += forest[c][y] 
    
    for c in range(0, x):
        tallestup = tallestup and int(tree) > int(forest[c][y])
        up += forest[c][y]
    visible = tallestleft or tallestright or tallestup or tallestdown

    return visible 

def isVisible(x,y,forest):
    if isBorder(x, y, forest):
        return 1
    elif compareViz(x, y, forest):
        return 1
    return 0

for x,y in enumerate(sys.stdin):
    forest[x] = dict(enumerate(y.strip("\n")))

numVisible = 0

for x in forest:
    for y in forest.keys():
        numVisible += isVisible(x,y, forest)
print(numVisible)