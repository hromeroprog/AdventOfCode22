
with open("input.txt") as file:
    lines = [line[:-1] for line in file.readlines()]

n_chests = (len(lines[0])+1) // 4
chests = {(i+1):[] for i in range(n_chests)}

cond = False
for line in lines:
    if not cond:
        if line[1] == '1':
            cond = True
            for k in chests:
                chests[k] = chests[k][::-1]
        else:
            for i,char in enumerate(line):
                if char not in "[] ":
                    print(char, "char")
                    chest = ((i-1)//4)+1
                    chests[chest].append(char)
                
    else:
        if len(line)>0:
            num = int(line.split()[1])
            from_ = int(line.split()[3])
            to = int(line.split()[5])
            if num == 1:
                chests[to].append(chests[from_].pop())
            else:
                chests[to] += chests[from_][-num:]
                chests[from_] = chests[from_][:-num]

result = ""
for k in chests:
    result += chests[k][-1]
    