import numpy as np

# input in matrix
grid = np.array([list(x.strip()) for x in open("input.txt", 'r')], int)

# get number of rows and cols
nrow, ncol = np.shape(grid)

# outside ring trees are visible
visible_trees = (ncol * 2) + (nrow * 2) - 4 
best_view_score = 1

for r in range(1, nrow - 1): # loop through inside trees
	for c in range(1, ncol - 1):
		hight = grid[r, c]
		#find trees to edge
		trees_left = grid[r, :c]
		trees_right = grid[r, c + 1:]
		trees_up = grid[:r, c]
		trees_down = grid[r + 1:, c]
		# determine tallest tree in each direction.
		tallest_tree_left = max(trees_left)
		tallest_tree_right = max(trees_right)
		tallest_tree_up = max(trees_up)
		tallest_tree_down = max(trees_down)
		# count trees visible from any direction id they are higher than other trees in that direction
		if hight > tallest_tree_left or hight > tallest_tree_right or hight > tallest_tree_up or hight > tallest_tree_down: 
			visible_trees += 1
		
		# count visible trees looking left
		vis_tree_left = 0
		for steps in range(len(trees_left)):
			vis_tree_left += 1
			if trees_left[len(trees_left) - 1 - steps] >= hight:
				break
		# count visible trees looking right
		vis_tree_right = 0
		for steps in range(len(trees_right)):
			vis_tree_right += 1
			if trees_right[steps] >= hight:
				break
		# count visible trees looking up
		vis_tree_up = 0
		for steps in range(len(trees_up)):
			vis_tree_up += 1
			if trees_up[len(trees_up) - 1 - steps] >= hight:
				break
		# count visible trees looking down
		vis_tree_down = 0
		for steps in range(len(trees_down)):
			vis_tree_down += 1
			if trees_down[steps] >= hight:
				break
		
		view_score = vis_tree_left * vis_tree_right * vis_tree_up * vis_tree_down
		if view_score > best_view_score:
			best_view_score = view_score

print ("visible trees =", visible_trees)
print ("best view score =", best_view_score )
