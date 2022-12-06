import sys
A = 1 #Rock
B = 2 #Paper
C = 3 #Scissors

X = 1 #Rock
Y = 2 #Paper
Z = 3 #Scissors

WIN = 6
DRAW = 3
LOSE = 0

strategy = { "A": "Y", "B":"X", "C":"Z"}
rounds = [("A","Y"), ("B", "X"), ("C","Z")]

def winRules(they, me):
    if eval(they) == eval(me):
        return DRAW    
    elif they == 'A':
        if me == 'Y':
            return WIN
        else:
            return LOSE
    elif they == 'B':
        if me == 'Z':
            return WIN
        else:
            return LOSE
    elif they == 'C':
        if me == 'X':
            return WIN
        else:
            return LOSE
    else: 
        return 0
    
def scoreRound(round):
    they = round[0]
    me = round[1]
    me_value = eval(me)
    battle_value = winRules(they, me)
    return me_value + battle_value

total_points = 0
for line in sys.stdin:
    round = line.replace('\n','').split(" ")
    score = scoreRound(round)
    total_points += score 

print(total_points)