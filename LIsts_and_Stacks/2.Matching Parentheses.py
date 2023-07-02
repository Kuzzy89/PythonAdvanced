line = input()

s = []
for i in range(len(line)):
    ch = line[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        start_index = s.pop()
        end_index = i + 1
        print(line[start_index:end_index])
