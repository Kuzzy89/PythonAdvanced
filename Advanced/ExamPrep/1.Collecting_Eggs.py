from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))

filled_boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg == 13:
        swap_egg = papers.popleft()
        papers.appendleft(paper)
        papers.append(swap_egg)
        continue

    if egg <= 0:
        papers.append(paper)
        continue

    if egg + paper <= 50:
        filled_boxes += 1


if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if papers:
    print(f'Pieces of paper left: {", ".join([str(x) for x in papers])}')
