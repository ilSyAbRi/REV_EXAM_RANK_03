def bracket_validator(s: str) -> bool:
    open_brackets = []

    for c in s:
        if c == '{':
            open_brackets.append('{')
        elif c == '[':
            open_brackets.append('[')
        elif c == '(':
            open_brackets.append('(')

        if c == '}':
            if open_brackets[-1] != '{':
                return False
            open_brackets.pop()
        elif c == ')':
            if open_brackets[-1] != '(':
                return False 
            open_brackets.pop()
        elif c == ']':
            if open_brackets[-1] != '[':
                return False
            open_brackets.pop()
    return True

print(bracket_validator("()"))
