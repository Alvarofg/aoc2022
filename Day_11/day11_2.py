import sys
import re

monkeys_data = "".join(sys.stdin).split("\n\n")

class Monkey():
    def __init__(self, data):
        self.id = self.parseId(data[0])
        self.items = self.parseItems(data[1])
        self.operation = self.parseOperation(data[2])
        self.test = self.parseTest(data[3:6])
        self.inspectCount = 0

    def parseId(self, line):
        return re.findall("\d+", line)[0]

    def parseItems(self, line):
        return [int(x) for x in re.findall("\d+", line)][::-1]

    def parseOperation(self, line):
        operator = re.findall("[+*]", line)[0]
        term = [ int(x)  for x  in re.findall("(?![*]\s)\d+", line)]

        if len(term):
            if operator == '+':
                f = lambda x : x + term[0]
            else:
                f = lambda x : x * term[0]
        else:
            if operator == '+':
                f = lambda x : x + x
            else:
                f = lambda x : x * x
        return  f 

    def parseTest(self, lines):
        self.divisor = int(re.findall("\d+",lines[0])[0])
        self.true = int(re.findall("\d+",lines[1])[0])
        self.false = int(re.findall("\d+",lines[2])[0])
        f = lambda x : self.false if x % self.divisor else self.true
        return f

    def receive(self, item):
        self.items.insert(0, item)
    
    def send(self, dest, item):
        self.l[dest].receive(item)
        pass

    def relax(self, worry):
        factor = N
        return int(worry % factor)

    def round(self):
        for itemx in range(len(self.items)):
            item_worry = self.items.pop(-1)  
            item_worry = self.operation(item_worry)
            item_worry = self.relax(item_worry)
            dest = self.test(item_worry)
            self.send(dest, item_worry)
            self.inspectCount +=1

def parseInput(input):
    monkeys =  dict()
    for data in input:
        attribs = data.split("\n")
        id = re.findall("\d+", attribs[0])[0]
        monkeys[int(id)] = Monkey(attribs)
        monkeys[int(id)].l = monkeys
    return monkeys

N = 1

monkeys = parseInput(monkeys_data)
for m,v in monkeys.items():
    N *= v.divisor 

rounds = 10000
for r in range(rounds):
    for id, monkey in monkeys.items():
        monkey.round()
activity = []
for m, monkey in monkeys.items():
    activity.append(monkey.inspectCount)

activity.sort(reverse = True)
print("Part 2:", activity[0] * activity[1])