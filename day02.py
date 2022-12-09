def calcTotalScore(strategyFile):
    valuesPlayerShapes = {"X": 1, "Y": 2, "Z": 3}
    strategyWinMap = {"A": "Y", "B": "Z", "C": "X"}
    strategyDrawMap = {"A": "X", "B": "Y", "C": "Z"}
    strategyLostMap = {"A": "Z", "B": "X", "C": "Y"}
    sumScore = 0
    with open(strategyFile, "r") as file:
        for line in file:
            if strategyWinMap[line[0]] == line[2]:
                sumScore += 6 + valuesPlayerShapes[line[2]]
            elif strategyDrawMap[line[0]] == line[2]:
                sumScore += 3 + valuesPlayerShapes[line[2]]
            elif strategyLostMap[line[0]] == line[2]:
                sumScore += valuesPlayerShapes[line[2]]
    print("total score: ", sumScore)

def calcUltraScore(strategyFile):
    roundEndValues = {"X": 0, "Y": 3, "Z": 6}
    strategyWinMap = {"A": "Y", "B": "Z", "C": "X"}
    strategyDrawMap = {"A": "X", "B": "Y", "C": "Z"}
    strategyLostMap = {"A": "Z", "B": "X", "C": "Y"}
    valuesPlayerShapes = {"X": 1, "Y": 2, "Z": 3}

    sumScore = 0

    with open(strategyFile, "r") as file:
        for line in file:
            if roundEndValues[line[2]] == 0:
                #lost
                playerWeapon = strategyLostMap[line[0]]
                sumScore += valuesPlayerShapes[playerWeapon]
            elif roundEndValues[line[2]] == 3:
                #draw
                playerWeapon = strategyDrawMap[line[0]]
                sumScore += 3 + valuesPlayerShapes[playerWeapon]
            elif roundEndValues[line[2]] == 6:
                #win
                playerWeapon = strategyWinMap[line[0]]
                sumScore += 6 + valuesPlayerShapes[playerWeapon]
    print("total score: ", sumScore)


print("-------- Example guide, part 1  ------------")
calcTotalScore("testday02.out")

print("-------- Example guide, part 2  ------------")
calcUltraScore("testday02.out")

print("-------- Official guide, part 1 ------------")
calcTotalScore("day02.out")

print("-------- Official guide, part 2 ------------")
calcUltraScore("day02.out")


