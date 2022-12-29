with open("input.txt") as file:
    rucksacks = [line[:-1] for line in file.readlines()]

total = 0
for i in range(0,len(rucksacks), 3):
    sol = (set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2]))).pop()
    if ord(sol) < ord('a'):
        total += ord(sol)- ord('A') + 27
    else:
        total += ord(sol) - ord('a') +1
    