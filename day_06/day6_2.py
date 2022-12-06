import sys

def isMarker(text):
    return len(text) == len(set(text))
    
def parseBuffer(buffer):
    for i in range(len(buffer) -14):
        marker = isMarker(buffer[i:i+14])
        if marker:
            return i+14 

for line in sys.stdin:
    print(parseBuffer(line))