def echo_validator(text: str) -> bool:
    clean = ""
    for c in text:
        if c.isalpha():
            clean += c.lower()
    if clean == "":
        return False
    return clean == clean[::-1]

print(echo_validator("  "))
