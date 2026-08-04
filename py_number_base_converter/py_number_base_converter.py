def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    
    supported: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not  2 <= from_base <= 36:
        return "ERROR"
    if not 2 <= to_base <= 36:
        return "ERROR"

    try:
        decimal = int(number,from_base)
    except ValueError:
        return "ERROR"
    
    if decimal == 0:
        return "0"
    result = ""
    sign = 0
    if decimal < 0:
        sign = 1
        decimal = abs(decimal)
    while decimal > 0:
        result =  supported[decimal % to_base] + result
        decimal //= to_base

    if sign == 1:
        result = "-" + result

    return result

print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("35", 10, 36))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))

