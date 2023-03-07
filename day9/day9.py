pos_tail_x = pos_tail_y = pos_head_x = pos_head_y = 0
visited = [(pos_tail_x, pos_tail_y)]

def move_tail():
	global visited
	global pos_head_x, pos_head_y, pos_tail_x, pos_tail_y
	visited.append((pos_tail_x, pos_tail_y))
	dist_vert = pos_head_y - pos_tail_y
	dist_hori = pos_head_x - pos_tail_x

	if dist_hori > 1 and dist_vert > 0:
		pos_tail_x += 1
		pos_tail_y = pos_head_y
	if dist_hori < -1 and dist_vert > 0:
		pos_tail_x -= 1
		pos_tail_y = pos_head_y
	if dist_vert > 1 and dist_hori > 0:
		pos_tail_y += 1
		pos_tail_x = pos_head_x
	elif dist_vert < -1 and dist_hori > 0:
		pos_tail_y -= 1
		pos_tail_x = pos_head_x

	if dist_hori > 1:
		pos_tail_x += 1
	if dist_hori < -1:
		pos_tail_x -= 1
	if dist_vert > 1:
		pos_tail_y += 1
	if dist_vert < -1:
		pos_tail_y -= 1
	
def move_head(direction):
	global pos_head_x, pos_head_y, pos_tail_x, pos_tail_y
	if direction == 'R':
		pos_head_x += 1
	if direction == 'L':
		pos_head_x -= 1
	if direction == 'U':
		pos_head_y += 1
	if direction == 'D':
		pos_head_y -= 1

file = open("inputex.txt", 'r')
for line in file:
	line = line.strip()
	steps = int(line[2])
	while steps != 0:
		move_head(line[0])
		move_tail()
		steps -= 1

# print(visited)
# print(set(visited))
print("unique positions visited by tail =", len(set(visited)))
# works for example
# 3012 too low
# 2871 too low