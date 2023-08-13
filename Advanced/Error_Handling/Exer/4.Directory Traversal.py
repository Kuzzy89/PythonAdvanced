from os import listdir
from os.path import isdir, join


def directory_traversal(path, files_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), files_by_ext)
        else:
            extension = element.split(".")[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


result = {}
directory_traversal("./", result)
final_result = []
sorted_result = sorted(result.items(), key=lambda x: x[0])

for key, values in sorted_result:
    final_result.append(f".{key}")

    for value in sorted(values):
        final_result.append(f"- - -{value}")

with open("./report.txt", "w") as file:
    file.write("\n".join(final_result))
