def getMostCalories(file):
  #calculates solution for part 1
  caloriesArray = []
  sumCaloriesArray = []
  sumCalories = 0
  name = ""
  with open(file, "r") as file:
    name = file.name
    for line in file:
      if line != "\n":
        sumCalories += int(line)
      else:
        sumCaloriesArray.append(sumCalories)
        sumCalories = 0
  print(name)
  print("Solution part 1:")
  print(max(sumCaloriesArray))
  sumCaloriesArray.sort(reverse=True)
  print("Solution part 2:")
  print(sumCaloriesArray[0]+sumCaloriesArray[1]+sumCaloriesArray[2])

 

getMostCalories("testday01.out")
getMostCalories("day01.out")
