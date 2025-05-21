# A Number Walks Into a Base...
print(0b10 + 0o10 + 0x10)
"""
Python allows us to write integers in different bases using specific prefixes: 0b for binary, 0o for octal, and 0x for hexadecimal. In the given code, we are adding three such numbers:
0b10 is binary for 2
0o10 is octal for 8
0x10 is hexadecimal for 16
Putting it all together, the expression becomes 2 + 8 + 16, which equals 26
"""

# A Slice of Confusion
text = "Python"[::-1][::-1]
print(text)
"""
This might look like it's doing something fancy, but it’s just a double reversal.

"Python"[::-1] reverses the string: "nohtyP"
Then, [::-1] again reverses it back to the original: "Python"

So the final result is just "Python"
"""

# List Illusions
a = [1, 2, 3]
b = a
a.append(4)
print(b)
"""
Both 'a' and 'b' refer to the same list object in memory.
So when 'a' is modified, 'b' reflects those changes too.

The output will be: [1, 2, 3, 4]
"""

# Set the Record Straight
print({1, 2, 3} == {3, 2, 1})
"""
Sets in Python are unordered collections of unique elements.

{1, 2, 3} and {3, 2, 1} contain the same elements, so they are considered equal.

The output will be: True
"""

# Plus Minus Sanity
class Strange:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val * other.val

    def __radd__(self, other):
        return self.val + other

a = Strange(3)
b = Strange(2)

print(a + b)
print(10 + a)
print(a + 10)
"""
a + b → calls a.__add__(b) → 3 * 2 = 6
10 + a → calls a.__radd__(10) → 3 + 10 = 13
a + 10 → a.__add__(10) → 10 has no `.val` → AttributeError

So:
6
13
[raises AttributeError]
"""



