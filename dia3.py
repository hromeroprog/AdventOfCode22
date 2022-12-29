with open("input.txt") as file:
    rucksacks = [line[:-1] for line in file.readlines()]

total = 0
for r in rucksacks:
    l = len(r)//2
    first = r[:l]
    second = r[l:]
    sol = list(set([letter for letter in first]).intersection(set([letter for letter in second])))[0]
    print(sol)
    if ord(sol) < ord('a'):
        add = ord(sol)- ord('A') + 27
        total += add
        print(f'sol = {sol} addinf {add}')
    else:
        total += ord(sol) - ord('a') +1
    