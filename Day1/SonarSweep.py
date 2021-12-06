f = open("InputSonarSweep.txt", "r")
lines = f.readlines()
f.close()

measurements = [int(i) for i in lines]
depthIncrease = 0
depthIncreaseFiltered = 0
prevWindowSum = 0
for line, nextLine, nextNextLine in zip(measurements, measurements[1 : ] + measurements[ : 1], measurements[2 : ] + measurements[ : 2]):
    windowSum = line+nextLine+nextNextLine
    if windowSum > prevWindowSum: depthIncreaseFiltered += 1
    prevWindowSum = windowSum
    if nextLine > line: depthIncrease += 1
    
print('Part 1 solution:', depthIncrease)
#We have to reduce the part 2 solution by 1 in order to exclude the increase because of no first window.
print('Part 2 solution:', depthIncreaseFiltered-1)