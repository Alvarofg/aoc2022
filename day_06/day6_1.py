import sys

def isMarker(text):
    return len(text) == len(set(text))
    
def parseBuffer(buffer):
    for i in range(len(buffer) -4):
        marker = isMarker(buffer[i:i+4])
        if marker:
            return i+4 

for line in sys.stdin:
    print(parseBuffer(line))