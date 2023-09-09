from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))

challenges = deque(map(int, input().split()))

while tools and substances and challenges:
    a_tool = tools.popleft()
    a_substance = substances[-1]
    result = a_tool * a_substance

    if result in challenges:
        challenges.remove(result)
        substances.pop()

    else:
        a_substance -= 1

        if a_substance > 0:
            substances[-1] = a_substance
        else:
            substances.pop()

        a_tool += 1
        tools.append(a_tool)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")