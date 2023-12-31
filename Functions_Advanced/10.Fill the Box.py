def fill_the_box(height, length, width, *args):
    volume = height * length * width
    el_sum = 0
    for el in args:
        if el == "Finish":
            break
        if volume >= el:
            volume -= el
        else:
            el -= volume
            el_sum += el
            volume = 0

    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {el_sum} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))