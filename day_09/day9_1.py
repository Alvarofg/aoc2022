import sys
import operator

head = set()
tail = set()
head.add((0,0))
tail.add((0,0))

def walkTail(hpos1, tpos1):
    
    hx, hy = hpos1
    tx, ty = tpos1
    dx, dy = abs(hx-tx), abs(hy-ty)
    if dx <= 1 and dy <=1:
        return tpos1
    
    if dx >1 or dy >1:
        if dx >1:
            inc = 1 if hx - tx > 0 else -1
            tx = tx + inc
            ty = hy
        if dy >1:
            inc = 1 if hy - ty > 0 else -1
            tx = hx
            ty = ty + inc
    return tx,ty

def walkHead(hpos, tpos, line, tail):
    d,n = tuple(l for l in line.strip().split())
    n = int(n)
    x, y = hpos
    if d in ['L', 'D']: 
        inc = -1
    else:
        inc = 1
    for c in [n for n in range(0,n)]:
        if d in ['R', 'L']:
            x += inc
            tpos = walkTail((x,y), tpos)
            tail.add(tpos)
            pass
    
        if d in ['U', 'D']:
            y += inc
            tpos = walkTail((x,y), tpos)
            tail.add(tpos)
    return ((x,y), tpos )

hpos = (0,0)
tpos = (0,0)
for line in sys.stdin:
    hpos, tpos = walkHead(hpos, tpos, line, tail)

print(len(tail))