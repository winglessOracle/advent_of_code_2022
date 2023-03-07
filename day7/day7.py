cwd = root = {}
stack = []

file = open('input.txt', 'r')

for line in file:
	line = line.strip()
	if line [0] == "$":
		if line [2] == "c":
			dir = line[5:]
			if dir == "/":
				cwd = root
				stack = []
			elif dir == "..":
				cwd = stack.pop()
			else:
				if dir not in cwd:
					cwd[dir] = {}
				stack.append(cwd)
				cwd = cwd[dir]
	else:
		x, y, = line.split()
		if x == "dir":
			if y not in cwd:
				cwd[y] = {}
		else:
			cwd[y] = int(x)

print (root)

def solve(dir = root):
	if type(dir) == int:
		return (dir, 0)
	size = 0
	total = 0
	for child in dir.values():
		s, t = solve(child)
		size += s
		total += t
	if size <= 100000:
		total += size
	return (size, total)

print(solve()[1])