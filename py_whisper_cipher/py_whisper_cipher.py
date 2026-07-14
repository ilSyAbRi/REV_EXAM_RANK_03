


def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if c.isalpha() and c.islower():
            position = ord(c) - ord('a')
            data = ord('a') + ((position + shift) % 26)
            result += chr(data)
        elif c.isalpha() and c.isupper():
            position = ord(c) - ord('A')
            data = ord('A') + ((position + shift) % 26)
            result += chr(data)
        else:
            result += c
    return result

print(whisper_cipher("abc  ABC z Z",1))
