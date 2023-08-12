from string import punctuation


def count_symbols(line1):
    punctuations_symbols = set(punctuation)
    letters_count = 0
    punctuations_count = 0
    for symbol in line1:
        if symbol.isalpha():
            letters_count += 1
        elif symbol in punctuations_symbols:
            punctuations_count += 1
    return letters_count, punctuations_count


with open("./text1.txt", "r") as input_file, open("./output.txt", "w") as output_file:
    for i, line in enumerate(input_file):
        letters, punctuations = count_symbols(line)
        output_file.write(f"line {i + 1}: {line.strip()} ({letters}) ({punctuations})\n")
