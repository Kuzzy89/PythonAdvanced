def forecast(*data):
    result = []

    def add_location(type_of_location):
        locations = list(filter(lambda x: x[1] == type_of_location, data))
        [result.append(f"{l[0]} - {type_of_location}") for l in sorted(locations)]

    add_location("Sunny")
    add_location("Cloudy")
    add_location("Rainy")

    return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

