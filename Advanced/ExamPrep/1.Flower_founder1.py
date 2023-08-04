from collections import deque


def mark_words_letter(vow, consonant, word):
    if vow in word:
        word.remove(vow)
    if consonant in word:
        word.remove(consonant)


vowels = deque(input().split())
consonants = input().split()
found_flower = None
rose = set("rose")
tulip = set("tulip")
lotus = set("lotus")
daffodil = set("daffodil")

while vowels and consonants:
    vow = vowels.popleft()
    consonant = consonants.pop()

    mark_words_letter(vow, consonant, rose)
    if len(rose) == 0:
        found_flower = "rose"
        break

    mark_words_letter(vow, consonant, tulip)
    if len(tulip) == 0:
        found_flower = "tulip"
        break

    mark_words_letter(vow, consonant, lotus)
    if len(lotus) == 0:
        found_flower = "lotus"
        break

    mark_words_letter(vow, consonant, daffodil)
    if len(daffodil) == 0:
        found_flower = "daffodil"
        break

if found_flower is None:
    print(f"Cannot find any word!")
else:
    print(f"Word found: {found_flower}")

if vowels:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(str(x) for x in consonants)}")
