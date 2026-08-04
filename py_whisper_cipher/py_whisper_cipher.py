


def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if c.isalpha() and c.islower():
            position = ord(c) - ord("a")
            get_shifting = (position + shift) % 26
            get_right_pos = ord("a") + get_shifting
            answer = chr(get_right_pos)
            result += answer
        elif c.isalpha() and c.islower()
            position = ord(c) - ord("A")
            get_shifting = (position + shift) % 26
            get_right_pos = ord("A") + get_shifting
            answer = chr(get_right_pos)
            result += answer
        else:
            result += c
    return result


