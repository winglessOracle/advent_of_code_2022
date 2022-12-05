priority = 0
with open ('input.txt') as file:
	rucksack = file.read().strip().split('\n')
for rs in rucksack:
	l = len(rs)
	left = rs[:l // 2]
	right = rs[l // 2:]
	for item in left:
		if item in right:
			if item.islower():
				value = ord(item) - 96
			else:
				value = ord(item) - 64 + 26
	priority += value
print('prio first task is:', priority) 

priority2 = i = value = 0
while i < len(rucksack):
	bag1 = rucksack[i]
	bag2 = rucksack[i + 1]
	bag3 = rucksack[i + 2]
	for badge in bag1:
		if badge in bag2 and badge in bag3:
			if badge.islower():
				value = ord(badge) - 96
			else:
				value = ord(badge) - 64 + 26
	priority2 += value
	i += 3
print('prio second task is:', priority2) 
