f = open("Dive.txt", "r")
lines = f.readlines()
f.close()
horizontal = 0
#This is the depth used for Part1
depth1 = 0
#This is the depth used for Part2
depth2 = 0
aim = 0

for line in lines:
    command = line.split(" ")[0]
    units = int(line.split(" ")[1])
    if command == 'forward': 
        horizontal += units
        depth2 += aim*units
    elif command == 'down': 
        depth1 += units
        aim += units
    else: 
        depth1 -= units
        aim -= units

print('My final position for Part1 is:')
print('Horizontal: ',horizontal,' Depth: ',depth1)
print('Part 1 solution: ',horizontal*depth1)
print('My final position for Part2 is:')
print('Horizontal: ',horizontal,' Depth: ',depth2)
print('Part 2 solution: ',horizontal*depth2)