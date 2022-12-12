import numpy as np

with open ('inputtemp.txt', 'r') as file:
	lines = file.read().strip().split()

grid = 

print(lines)

# grid = [list(map(int, list(line))) for line in lines]

# c = len(grid[0])
# r = len(grid)

# trees = 0
# for x in range(c)
# 	for y in range(r)
# 		hight = grid[x, y]

# 		if y == 0 or np.amax(grid[x, :j]) < h:
# 			trees += 1



# #outside ring
# ring = 2 * len(lines[0]) + 2 * len(lines) - 4
# coordinates = []

# # top
# r = c = 1
# while c < len(lines[0]) - 1:
# 	while r < len(lines) - 1:
# 		if lines[r][c] > lines[r - 1][c]:
# 			coordinates.append((r,c))
# 			r += 1
# 		else:
# 			r += 1
# 	r = 1
# 	c += 1

# # left
# r = c = 1
# while r < len(lines) - 1:
# 	while c < len(lines[0]) - 1:
# 		if lines[r][c] > lines[r][c - 1]:
# 			coordinates.append((r,c))
# 			c += 1
# 		else:
# 			c += 1
# 	c = 1
# 	r += 1

# # right
# r = 1
# c = len(lines[0]) - 1
# while r < len(lines) - 1:
# 	while c < 0:
# 		if lines[r][c] > lines[r][c + 1]:
# 			coordinates.append((r,c))
# 			c -= 1
# 		else:
# 			c -= 1
# 	c = len(lines[0]) - 1
# 	r += 1

# #bottom
# r = len(lines) - 1
# c = 1
# while r < 0:
# 	while c < len(lines[0]) - 1:
# 		if lines[r][c] > lines[r + 1][c]:
# 			coordinates.append((r,c))
# 			r -= 1
# 		else:
# 			r -= 1
# 	r = len(lines) - 1
# 	c += 1

# unique_coordinates = len(set(coordinates))
# print (set(coordinates))
# print ("outside ring trees = ", ring)
# print ("visible trees = ", unique_coordinates + ring)
