import sys

def walkTail(head, curTail):
    hx, hy = head
    tx, ty = curTail
    dx, dy = abs(hx-tx), abs(hy-ty)
    if dx <= 1 and dy <=1:
        return curTail
    
    if( dx > 1 and dy > 1):
        inc = 1 if hx - tx > 0 else -1
        tx = tx + inc
        inc = 1 if hy - ty > 0 else -1
        ty = ty + inc
        return tx,ty
    
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

def walkHead(hpos, line):
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
        if d in ['U', 'D']:
            y += inc       
        new_head = x,y
        
        tpos[0] = walkTail(new_head, tpos[0]) 
        tailsets[0].add(tpos[0])
        for j in range(1, len(tpos)):
            tail = tpos[j-1]
            tpos[j] = walkTail(tail, tpos[j])
            tailsets[j].add(tpos[j])
   
    return (new_head)

hpos = (0,0)
tpos_origin = (0,0)
knots = 9
tpos = [(0,0)]*knots
tailsets = [set() for c in range(knots)]
for s in tailsets:
    s.add(tpos_origin)

for line in sys.stdin:
        hpos = walkHead(hpos, line)

lens = [len(s) for s in tailsets]

print("Part 1:", len(tailsets[0]))
print("Part 2:", len(tailsets[knots-1]))

# chart = [".........................."]*20
# for s in tailsets[8]:
#     x, y = s
#     # print(x, y) 
#     tmp = list(chart[y])
#     tmp[x] = "#"
#     chart[y] =  "".join(tmp)

# tmp = list(chart[0])
# tmp[0] = "s"
# chart[0] =  "".join(tmp)
# print("\n".join(chart[::-1]))
