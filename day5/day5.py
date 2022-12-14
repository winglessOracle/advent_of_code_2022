import re

stacks = []
instructions = []

file = open('input5.txt', 'r')
for line in file:
	if line == '\n':
		break
	stacks.append([line[k * 4 + 1] for k in range(len(line) // 4)])
stacks.pop()
stacks = zip(*stacks)
stacks = ([list("".join(c).strip()[::-1]) for c in stacks])

# for row in stacks:
# 	print (row)

for line in file:
	move, source, dest = map(int, re.findall("\d+", line))
	stacks[dest - 1].extend(stacks[source - 1][-move:][::-1])
	stacks[source - 1] = stacks[source -1 ][:-move]

output = ("".join([a[-1] for a in stacks]))
print (output)