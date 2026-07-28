def bracket_validator(s: str) -> bool:
    stack = []
    dic = {"}":"{", "]":"[", ")":"("}
    for c in s:
        if c in "{[(":
            stack.append(c)

        if c in "}])":
            if stack and dic[c] == stack[-1]:
                stack.pop()

    return len(stack) == 0


print(bracket_validator(""))
