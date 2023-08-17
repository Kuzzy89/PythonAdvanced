def even_odd(*args):
    filtered_command = args[-1]
    parity = 0 if filtered_command == "even" else 1
    result = []

    for i in range(len(args) - 1):
        number = args[i]
        if number % 2 == parity:
            result.append(number)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))