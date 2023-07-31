def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    for kid_data in args:
        number, type_kids = kid_data.split("-")



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
