import sys
A = 1 #Rock
B = 2 #Paper
C = 3 #Scissors

X = 1 # Lose
Y = 2 # Draw
Z = 3 # Win

WIN = 6
DRAW = 3
LOSE = 0

strategy = { "A": "Y", "B":"X", "C":"Z"}
rounds = [("A","Y"), ("B", "X"), ("C","Z")]

def Win(they):
    if they == 'A':
        return 'B'
    elif they == 'B':
        return 'C'
    elif they == 'C':
        return 'A'

def Lose(they):
    if they == 'A':
        return 'C'
    elif they == 'B':
        return 'A'
    elif they == 'C':
        return 'B'

def Draw(they):
    return they

def winRules(they, me):
    if eval(they) == eval(me):
        return DRAW    
    elif they == 'A':
        if me == 'B':
            return WIN
        else:
            return LOSE
    elif they == 'B':
        if me == 'C':
            return WIN
        else:
            return LOSE
    elif they == 'C':
        if me == 'A':
            return WIN
        else:
            return LOSE
    else: 
        return 0

def decide(decision):
    if decision == 'X':
        return Lose 
    elif decision == 'Y':
        return Draw
    else: 
        return Win

def scoreRound(round):
    they = round[0]
    decision = round[1]
    me = decide(decision)(they)
    me_value = eval(me)
    battle_value = winRules(they, me)
    return me_value + battle_value

total_points = 0
for line in sys.stdin:
    round = line.replace('\n','').split(" ")
    score = scoreRound(round)
    total_points += score 

print(total_points)