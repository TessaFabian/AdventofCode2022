def getMostCalories(file):
  caloriesArray = []
  sumCaloriesArray = []
  sumCalories = 0
  with open(file, "r") as file:
    for line in file:
      if line != "\n":
        sumCalories += int(line)
      else:
        sumCaloriesArray.append(sumCalories)
        sumCalories = 0
  sumCaloriesArray.sort()
  print(sumCaloriesArray[len(sumCaloriesArray)-1])



def buildCaloriesArray(file):
  caloriesArray = []
  with open(file, "r") as file:
    for line in file:
      if line == "\n":
        caloriesArray.append("n")
      else:
        caloriesArray.append(int(line))
  return caloriesArray

getMostCalories("testday01.out")
getMostCalories("day01.out")
