dir = total_dir = 0

with open ('input.txt', 'r') as file:
	lines = file.read().split('\n')
for parts in lines:
	if parts[1] == "cd":
	 	while parts[2] != "..":
	 		if parts[0].isnumeric:
				dir += int(parts[0])
		print (dir)




