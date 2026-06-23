
# Bracket Validator

## Assignment

Write a function that checks if the brackets in a string are valid.

A string is valid if every opening bracket has a matching closing bracket in the correct order.

Allowed brackets:

- `()`
- `[]`
- `{}`

---

## Function Signature

```python
def bracket_validator(s: str) -> bool:
```

---

## Examples

### Example 1

Input:

```python
bracket_validator("()")
```

Output:

```python
True
```

### Example 2

Input:

```python
bracket_validator("()[]{}")
```

Output:

```python
True
```

### Example 3

Input:

```python
bracket_validator("(]")
```

Output:

```python
False
```

### Example 4

Input:

```python
bracket_validator("([)]")
```

Output:

```python
False
```

### Example 5

Input:

```python
bracket_validator("{[]}")
```

Output:

```python
True
```

### Example 6

Input:

```python
bracket_validator("hello(world)")
```

Output:

```python
True
```

### Example 7

Input:

```python
bracket_validator("((())")
```

Output:

```python
False
```

### Example 8

Input:

```python
bracket_validator("")
```

Output:

```python
True
```

---

## Rules

- Every opening bracket must have a matching closing bracket.
- Brackets must be closed in the correct order.
- Non-bracket characters should be ignored.
- An empty string is considered valid.

---

## Expected Results

| Input | Output |
|--------|--------|
| `()` | `True` |
| `()[]{}` | `True` |
| `(]` | `False` |
| `([)]` | `False` |
| `{[]}` | `True` |
| `hello(world)` | `True` |
| `((())` | `False` |
| `""` | `True` |

