chars = ("-", ",", ".", "!", "?")
with open("./text1.txt", "r") as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for char in chars:
                result = result.replace(char, "@")
            print(result)
