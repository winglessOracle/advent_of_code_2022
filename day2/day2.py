#First part functions

# shape = 0
# win = 0
# total = 0

# def shape(fileName, x, y, z):
# 	shape = 0
	
# 	file =  open (fileName)
# 	text = file.read()
# 	for char in text:
# 		if char == x:
# 			shape += 1
# 		if char == y:
# 			shape += 2
# 		if char == z:
# 			shape += 3
# 	return (shape) 

# def win(fileName):
# 	round_win = total_win = 0
# 	with open ('input.txt') as f:
# 		file = f.readlines()
# 		for line in file:
# 			if (line.find('A') != -1 and line.find('Y') != -1) or (line.find('B') != -1 and line.find('Z') != -1) or (line.find('C') != -1 and line.find('X') != -1):
# 				round_win = 6
# 			if (line.find('A') != -1 and line.find('X') != -1) or (line.find('B') != -1 and line.find('Y') != -1) or (line.find('C') != -1 and line.find('Z') != -1):
# 				round_win = 3
# 			total_win += round_win
# 			round_win = 0
# 	return (total_win)

# print ("shape", shape('input.txt', 'X', 'Y', 'Z'))
# print ("win", win('input.txt'))
# print ("total", shape('input.txt', 'X', 'Y', 'Z') + win('input.txt'))

#############################################################################################
#First part short

# total = shape = win =0 
# with open ('input.txt') as f:
# 	file = f.readlines()
# for line in file:
# 	if (line.find('A') != -1 and line.find('Y') != -1) or (line.find('B') != -1 and line.find('Z') != -1) or (line.find('C') != -1 and line.find('X') != -1):
# 		shape = win = 6
# 	if (line.find('A') != -1 and line.find('X') != -1) or (line.find('B') != -1 and line.find('Y') != -1) or (line.find('C') != -1 and line.find('Z') != -1):
# 		win = 3
# 	if line.find('X') != -1:
# 		shape = 1
# 	if line.find('Y') != -1:
# 		shape = 2
# 	if line.find('Z') != -1:
# 		shape = 3
# 	total = total + win + shape
# 	print("win",win, "shape",shape)
# 	shape = win = 0
# 	print("total:",total)

##################################################################################################
# Second part

total = shape = 0 
with open ('input.txt') as f:
	file = f.readlines()
for line in file:
	if line.find('Z') != -1:
		if line.find('A') != -1:
			shape = 2 + 6
		elif line.find('B') != -1:
			shape = 3 + 6
		else:
			shape = 1 + 6
	if line.find('Y') != -1:
		if line.find('A') != -1:
			shape = 1 + 3
		elif line.find('B') != -1:
			shape = 2 + 3
		else:
			shape = 3 + 3
	if line.find('X') != -1:
		if line.find('A') != -1:
			shape = 3
		elif line.find('B') != -1:
			shape = 1
		else:
			shape = 2
	total += shape
	shape = 0
print("total:",total)
