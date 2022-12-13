import numpy as np

#seperate and transpose first part
x = 0
stacks = []
with open ('input5.txt', 'r') as file:
	lines = file.read().split('\n')
while x < 9:
	stacks.insert(0, lines[x])
	x += 1
stacks_t = np.array(stacks)

print (stacks_t)

