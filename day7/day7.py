cur_dir = total = step = count = 0
stackedpath = [0]
with open ('input.txt', 'r') as file:
	lines = file.read().strip().split()
for element in reversed(lines):
	if element.isdigit():
		cur_dir += int(element)
		if count != 0:
			stackedpath[count] += int(cur_dir)
	if element == "ls":
		print (cur_dir)
		if count != 0:
			cur_dir += int(stackedpath[count])
		if cur_dir <= 100000:
			total += cur_dir
		cur_dir = 0
	if element == "cd":
		if count != 0:
			stackedpath.pop()
			count -= 1
	if element == "..":
		stackedpath.append(cur_dir)
		count += 1
print ("total:", total)