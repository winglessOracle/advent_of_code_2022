count = count2 =0
with open ('input4.txt', 'r') as file:
	pairs = file.read().strip().split('\n')
for elf in pairs:
	first_range, second_range = elf.split(',')
	start_a, end_a = map(int, first_range.split('-'))
	start_b, end_b = map(int, second_range.split('-'))
	if (start_a <= start_b and end_a >= end_b) or (start_b <= start_a and end_b >= end_a):
		count+=1
	if start_a in range (start_b, end_b + 1) or end_a in range (start_b, end_b + 1) or start_b in range (start_a, end_a + 1) or end_b in range (start_a, end_a + 1):
		count2+=1
print(count, count2)
