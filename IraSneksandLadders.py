from random import randint
endTile = 100
position = 1
totalTurns = 0

snakeMouths = [34 ,25,47,65, 87, 91, 97]
snakeTails = [1, 5, 19, 52, 57, 61, 69]
ladderBottoms = [3, 6, 20, 36, 63, 68]
ladderTops = [51, 27, 70, 55, 95, 98]

def isSnake(space):
    index = 0
    if space in snakeMouths:
        index = snakeMouths.index(space)
        return snakeTails[index]
    else:
        return space

def isLadder(space):
    index = 0
    if space in ladderBottoms:
        index = ladderBottoms.index(space)
        return ladderTops[index]
    else:
        return space

def rollDice(space):
    diceVal = randint(1,6)
   # if (space + diceVal <= 100):
    space += diceVal
    return space


def nextTurn(space):
    space = rollDice(space)
    space = isLadder(space)
    space = isSnake(space)
    print(space)
    return space

while position < 100:
    position = nextTurn(position)
    totalTurns += 1

print("You Win")
print (totalTurns)