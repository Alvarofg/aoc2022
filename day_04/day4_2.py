import sys

def overlaps(x): #any overlap
    one = set( range( int(x[0][0]),int(x[0][1])+1 ))
    two = set( range( int(x[1][0]),int(x[1][1])+1 ))
    y = one.intersection(two)
    return len(y) > 0 

a = list(map( lambda y : (y[0].split("-"),y[1].split("-")), map(lambda x : x.replace("\n",'').split(","), sys.stdin)))
b = list(map( overlaps, a))
print(sum(b))
