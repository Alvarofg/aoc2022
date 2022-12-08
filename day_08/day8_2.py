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

def score(x,y, forest):
    tree = forest[x][y]
    border = len(forest)
    tallestleft = tallestright = tallestup = tallestdown =True

    right = left = up = down = 0
    for c in range(y+1, border):
        tallestright =  tallestright and tree > forest[x][c]
        right += 1
        if(not tallestright):
            if c==border:
                right +=1
            break

    for c in reversed(range(0,y)):
        tallestleft = tallestleft and tree > forest[x][c] 
        left +=  1
        if(not tallestleft):
            if(c == y):
                left += 1
            break
    
    for c in range(x+1, border):
        tallestdown = tallestdown and tree > forest[c][y] 
        down += 1
        if(not tallestdown):
            if(c == border):
                down += 1    
            break 
    
    for c in reversed(range(0, x)):
        tallestup = tallestup and tree > forest[c][y]
        up += 1
        if(not tallestup):
            if c== x:
                up += 1
                pass
            break

    return int(right * left * up * down) 


for x,y in enumerate(sys.stdin):
    forest[x] = dict(enumerate(y.strip("\n")))

dfo =''
maxScore = 0
for x in forest:
    for y in forest.keys():
        if not isBorder(x,y,forest):
            maxScore = max(maxScore, score(x,y, forest))
print(maxScore)
