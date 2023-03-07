import numpy as np

cycle = 0
x = 1
signal = 0

cycle_checks = [20, 60, 100, 140, 180, 220] 


# file = open("input.txt", "r")
# for line in file:
# 	line = line.split()
# 	if line[0] == "noop":
# 		cycle += 1
# 		if cycle in cycle_checks:
# 			signal += (cycle * x)
# 	elif line[0] == "addx":
# 		cycle += 1
# 		if cycle in cycle_checks:
# 			signal += (cycle * x)
# 		cycle += 1
# 		if cycle in cycle_checks:
# 			signal += (cycle * x)
# 		x += int(line[1])

# print ("part 1: total of measured signal strenghts =", signal)

crt = np.full((6, 40),'.')
crt_line = 0
def print_stuff(cycle, x):
	global crt, crt_line
	crt_line = 0
	if 40 / cycle < 1:
		crt_line += 1
		cycle = 0
	if cycle == x or cycle == x - 1 or cycle == x + 1:
		crt[crt_line, x] = "#"

file = open("inputex.txt", "r")
for line in file:
	line = line.split()
	if line[0] == "noop":
		cycle += 1
		print_stuff(cycle, x)
		if cycle in cycle_checks:
			signal += (cycle * x)
	elif line[0] == "addx":
		cycle += 1
		print_stuff(cycle, x)
		if cycle in cycle_checks:
			signal += (cycle * x)
		cycle += 1
		print_stuff(cycle, x)
		if cycle in cycle_checks:
			signal += (cycle * x)
		x += int(line[1])

print(crt)



