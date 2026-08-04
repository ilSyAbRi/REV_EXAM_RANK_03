def bracket_validator(s: str) -> bool:
    stack = []
    dic = {"}":"{", "]":"[", ")":"("}
    for c in s:
        if c in "{[(":
            stack.append(c)

        elif c in "}])":
            if not stack or dic[c] != stack[-1]:
                return False
            stack.pop()

    return len(stack) == 0


print(bracket_validator(")"))
