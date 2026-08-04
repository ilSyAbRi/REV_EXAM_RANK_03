
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
# Assignment examples
assert (result := cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])) == [
    "cat",
    "dog",
    "apple",
    "banana",
    "elephant",
], (
    f"Basic example failed:\n"
    f"expected: {['cat', 'dog', 'apple', 'banana', 'elephant']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])) == [
    "aaa",
    "AAA",
    "bbb",
    "BBB",
], (
    f"Case-insensitive ordering failed:\n"
    f"expected: {['aaa', 'AAA', 'bbb', 'BBB']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["hello", "world", "hi", "test"])) == [
    "hi",
    "test",
    "hello",
    "world",
], (
    f"Length and lexical ordering failed:\n"
    f"expected: {['hi', 'test', 'hello', 'world']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter([])) == [], (
    f"Empty list failed: expected [], got {result!r}"
)

assert (result := cryptic_sorter([""])) == [""], (
    f"Single empty string failed: expected [''], got {result!r}"
)


# Primary sort: shortest strings first
assert (result := cryptic_sorter(["aaaa", "b", "ccc", "dd"])) == [
    "b",
    "dd",
    "ccc",
    "aaaa",
], (
    f"Length sorting failed:\n"
    f"expected: {['b', 'dd', 'ccc', 'aaaa']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["python", "a", "rust", "go", "javascript"])) == [
    "a",
    "go",
    "rust",
    "python",
    "javascript",
], (
    f"Mixed length sorting failed:\n"
    f"expected: {['a', 'go', 'rust', 'python', 'javascript']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["bb", "", "a", "ccc"])) == ["", "a", "bb", "ccc"], (
    f"Empty string length sorting failed:\n"
    f"expected: {['', 'a', 'bb', 'ccc']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["12345", "1", "123", "12", "1234"])) == [
    "1",
    "12",
    "123",
    "1234",
    "12345",
], (
    f"Numeric-string length sorting failed:\n"
    f"expected: {['1', '12', '123', '1234', '12345']!r}\n"
    f"got:      {result!r}"
)


# Secondary sort: case-insensitive lexical order
assert (result := cryptic_sorter(["Dog", "cat", "Ant", "bee"])) == [
    "Ant",
    "bee",
    "cat",
    "Dog",
], (
    f"Case-insensitive lexical sorting failed:\n"
    f"expected: {['Ant', 'bee', 'cat', 'Dog']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["Z", "a", "B", "b", "A"])) == [
    "a",
    "A",
    "B",
    "b",
    "Z",
], (
    f"Single-character ordering failed:\n"
    f"expected: {['a', 'A', 'B', 'b', 'Z']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["Zoo", "apple", "Car", "bee"])) == [
    "bee",
    "Car",
    "Zoo",
    "apple",
], (
    f"Length should be checked before lexical order:\n"
    f"expected: {['bee', 'Car', 'Zoo', 'apple']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["cab", "ABC", "bac", "aaa"])) == [
    "aaa",
    "ABC",
    "bac",
    "cab",
], (
    f"Equal-length lexical sorting failed:\n"
    f"expected: {['aaa', 'ABC', 'bac', 'cab']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["Python", "banana", "APPLE!", "Cherry"])) == [
    "APPLE!",
    "banana",
    "Cherry",
    "Python",
], (
    f"Six-character lexical sorting failed:\n"
    f"expected: {['APPLE!', 'banana', 'Cherry', 'Python']!r}\n"
    f"got:      {result!r}"
)


# Stability: case-insensitively equal strings keep input order
assert (result := cryptic_sorter(["aaa", "AAA", "AaA", "aAa"])) == [
    "aaa",
    "AAA",
    "AaA",
    "aAa",
], (
    f"Stable order for equal keys failed:\n"
    f"expected: {['aaa', 'AAA', 'AaA', 'aAa']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["aA", "Aa", "AA", "aa"])) == [
    "aA",
    "Aa",
    "AA",
    "aa",
], (
    f"Stable mixed-case order failed:\n"
    f"expected: {['aA', 'Aa', 'AA', 'aa']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["cat", "dog", "cat", "Dog", "CAT"])) == [
    "cat",
    "cat",
    "CAT",
    "dog",
    "Dog",
], (
    f"Stable duplicate ordering failed:\n"
    f"expected: {['cat', 'cat', 'CAT', 'dog', 'Dog']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["Bob", "alice", "BOB", "ALICE"])) == [
    "Bob",
    "BOB",
    "alice",
    "ALICE",
], (
    f"Stable case-insensitive groups failed:\n"
    f"expected: {['Bob', 'BOB', 'alice', 'ALICE']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["same", "same", "same"])) == [
    "same",
    "same",
    "same",
], (
    f"Identical strings failed:\n"
    f"expected: {['same', 'same', 'same']!r}\n"
    f"got:      {result!r}"
)


# Digits and letters
assert (result := cryptic_sorter(["a2", "A1", "b0", "a0"])) == [
    "a0",
    "A1",
    "a2",
    "b0",
], (
    f"Letters and digits sorting failed:\n"
    f"expected: {['a0', 'A1', 'a2', 'b0']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["10", "02", "01", "20"])) == [
    "01",
    "02",
    "10",
    "20",
], (
    f"Numeric ASCII ordering failed:\n"
    f"expected: {['01', '02', '10', '20']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["b1", "A9", "a2", "B0"])) == [
    "a2",
    "A9",
    "B0",
    "b1",
], (
    f"Case-insensitive alphanumeric ordering failed:\n"
    f"expected: {['a2', 'A9', 'B0', 'b1']!r}\n"
    f"got:      {result!r}"
)


# Symbols use their ASCII order
assert (result := cryptic_sorter(["a1", "A!", "a0", "B0"])) == [
    "A!",
    "a0",
    "a1",
    "B0",
], (
    f"Symbol ASCII ordering failed:\n"
    f"expected: {['A!', 'a0', 'a1', 'B0']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["b!", "a?", "a!", "b?"])) == [
    "a!",
    "a?",
    "b!",
    "b?",
], (
    f"Punctuation ordering failed:\n"
    f"expected: {['a!', 'a?', 'b!', 'b?']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["##", "!!", "@@", "$$"])) == [
    "!!",
    "##",
    "$$",
    "@@",
], (
    f"ASCII symbol sorting failed:\n"
    f"expected: {['!!', '##', '$$', '@@']!r}\n"
    f"got:      {result!r}"
)


# Spaces are characters and have low ASCII values
assert (result := cryptic_sorter(["a ", " A", "!!", "  "])) == [
    "  ",
    " A",
    "!!",
    "a ",
], (
    f"Space ASCII ordering failed:\n"
    f"expected: {['  ', ' A', '!!', 'a ']!r}\n"
    f"got:      {result!r}"
)


# Combined cases
assert (
    result := cryptic_sorter(["Banana", "a", "DOG", "", "cat", "Apple", "dog", "bb"])
) == ["", "a", "bb", "cat", "DOG", "dog", "Apple", "Banana"], (
    f"Combined sorting criteria failed:\n"
    f"expected: {['', 'a', 'bb', 'cat', 'DOG', 'dog', 'Apple', 'Banana']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["zzz", "A", "aa", "BBB", "b", "AA", "aaa", ""])) == [
    "",
    "A",
    "b",
    "aa",
    "AA",
    "aaa",
    "BBB",
    "zzz",
], (
    f"Combined length, case, and stability failed:\n"
    f"expected: {['', 'A', 'b', 'aa', 'AA', 'aaa', 'BBB', 'zzz']!r}\n"
    f"got:      {result!r}"
)

assert (result := cryptic_sorter(["ccc", "BB", "a", "AAA", "bb", "C"])) == [
    "a",
    "C",
    "BB",
    "bb",
    "AAA",
    "ccc",
], (
    f"Multiple criteria ordering failed:\n"
    f"expected: {['a', 'C', 'BB', 'bb', 'AAA', 'ccc']!r}\n"
    f"got:      {result!r}"
)


print("All tests passed")

