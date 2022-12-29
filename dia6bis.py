
with open("input.txt") as file:
    line = [line[:-1] for line in file.readlines()][0]

processed = 0
l = []
s = set()
for char in line:
    processed += 1
    if len(l) == len(set(l)) and len(l) == 14:
        break
    l.append(char)
    if len(l) == 15:
        l.pop(0)
    
print(processed-1)

    