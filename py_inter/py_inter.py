def inter(s1: str, s2: str) -> str:
    result = ""
    data = ""
    for c in s1:
        if c in s2 and c not in data:
            result += c
            data += c
    return result

print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))
