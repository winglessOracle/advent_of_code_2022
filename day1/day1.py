cal = 0
num1 = [0]
with open ('day1.txt') as f:
    file = f.readlines()
    for line in file:
        if line  != '\n':
            cal += int(line)
        else:
            num1.append(cal)
            cal = 0
        num1.sort(reverse=True)
print("best elf =", num1[0])
print("Best three elves=",num1[0] + num1[1] + num1[2])