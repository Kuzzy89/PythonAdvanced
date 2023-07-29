def start_spring(**kwargs):
    result = ""
    spring_objects = {}

    for name, type in kwargs.items():
        if type not in spring_objects:
            spring_objects[type] = []
        spring_objects[type].append(name)

    #sorted_object_collection = sorted(spring_objects.items(), key=lambda x: x -(len(x[1]), x[0]))
    sorted_object_collection = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for sorted_object in sorted_object_collection:
        type_object = sorted_object[0]
        name_object = sorted_object[1]
        result += f"{type_object}:\n"
        for obj in sorted(name_object):
            result += f"-{obj}\n"
    return result.strip()

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
