def pattern_tracker(text: str) -> int:
    count = 0
    for c in range(len(text) - 1):
        first_digit = text[c]
        second_digit = text[c + 1]

        if text[c].isdigit() and text[c + 1].isdigit():
            if int(first_digit) + 1 == int(second_digit):
                count += 1
    return count

print(pattern_tracker("123"))
