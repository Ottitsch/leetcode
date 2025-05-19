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
