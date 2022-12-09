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

print("-------- Example guide  ------------")
calcTotalScore("testday02.out")

print("-------- Official guide  ------------")
calcTotalScore("day02.out")