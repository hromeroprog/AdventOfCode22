with open("input.txt") as file:
    lines = [line[:-1] for line in file.readlines()]

total = 0
for line in lines:
    elf1, elf2 = line.split(',')
    min1,max1 = list(map(int, elf1.split('-')))
    min2,max2 = list(map(int, elf2.split('-')))
    
    if (min1 <= min2 and min2 <= max1)  or (min2 <= min1 and min1 <= max2):
        print(elf1, 'overlapped', elf2)
        total += 1
    