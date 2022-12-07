with open ('input.txt', 'r') as file:
	line = file.read()

seq = ""
x = y = char = 0

while x < len(line):
	if line[x] not in seq:
		seq = seq + line[x]
	else:
		seq = ""
		y += 1 
		x = y
		char = y
	char += 1
	x += 1
	if len(seq) == 14:
		break

print (char)
