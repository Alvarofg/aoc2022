import sys
import re

def setPath(gPath, dir):
    if dir == "/":
        gPath = ['/']
    elif dir ==  '..':
        gPath.pop()
    elif dir not in ["..", '']:
        gPath.append(dir)
    return gPath

def parseCommand(gPath, line):
    dir = "".join(re.findall("(?<=\$\scd\s).+", line))
    gPath = setPath(gPath, dir)
    return gPath

gPath = ['/']
folders = dict()
for line in sys.stdin:
    if re.match("^[$]", line.strip("\n")):
        gPath = parseCommand(gPath, line)

    size = sum(list(map(int,re.findall("\d+", line))))
    if size > 0:
        dPath = ''
        for key in gPath:
            dPath += "_" + key
            if dPath in folders:
                folders[dPath] +=  size
            else:
                folders[dPath] = size
        
total =  folders['_/']
toDelete = 30000000 - 70000000 + int(total)
totals =  { key:value for (key,value) in folders.items() if value >= toDelete}
print("Part2: ", min(totals.values()))