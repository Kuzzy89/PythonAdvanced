string = input()

s = []

for v in string:
    s.append(v)

reversed_string = ""

while s:
    reversed_string += s.pop()

print(reversed_string)