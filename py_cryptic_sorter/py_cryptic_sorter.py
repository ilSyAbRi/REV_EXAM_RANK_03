
def vowels(str):
    vowels = ['a','e','u','i','o']
    count = 0
    for c in str:
        if c in vowels:
            count += 1

    return count

def checker(s1, s2):

    if len(s1) > len(s2):
        return True
    elif len(s1) < len(s2):
        return False

    if s1 > s2:
        return True
    elif s1 < s2:
        return False

    if vowels(s1) > vowels(s2):
        return True
    elif vowels(s1) < vowels(s2):
        return False

    return False

def cryptic_sorter(strings: list[str]) -> list[str]:
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if checker(strings[i].lower(), strings[j].lower()):
                strings[i], strings[j] = strings[j], strings[i]
    return strings

print(cryptic_sorter(["b","B","a"]))
