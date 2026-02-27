import re

# ============================================
# re.findall() usage examples
# ============================================

# --- 1. Simple word search ---
result = re.findall(r'cat', "my cat and kitten and another cat")
print(result)  # ['cat', 'cat', 'cat'] — found 3 times ("kitten" also contains "cat")

# --- 2. \d — digits ---
result = re.findall(r'\d+', "I am 25 years old, I have 3 cats and 12 fish")
print(result)  # ['25', '3', '12']

# --- 3. \d with quantity limits ---
# \d{2} — exactly 2 digits
result = re.findall(r'\d{2}', "1 23 456 7890")
print(result)  # ['23', '45', '78', '90']

# \d{2,3} — from 2 to 3 digits
result = re.findall(r'\d{2,3}', "1 23 456 7890")
print(result)  # ['23', '456', '789']

# --- 4. \w — letters, digits, underscore ---
result = re.findall(r'\w+', "Hello, world! How are you?")
print(result)  # ['Hello', 'world', 'How', 'are', 'you']

# --- 5. . (dot) — any character ---
result = re.findall(r'c.t', "cat cot cut cit cet")
print(result)  # ['cat', 'cot', 'cut', 'cit', 'cet']

# --- 6. * — zero or more repetitions ---
result = re.findall(r'ab*', "a ab abb abbb ac")
print(result)  # ['a', 'ab', 'abb', 'abbb', 'a']

# --- 7. + — one or more repetitions ---
result = re.findall(r'ab+', "a ab abb abbb ac")
print(result)  # ['ab', 'abb', 'abbb']

# --- 8. ? — zero or one time ---
result = re.findall(r'colou?r', "color and colour")
print(result)  # ['color', 'colour']

# --- 9. [...] — character class ---
# [aeiou] — vowels only
result = re.findall(r'[aeiou]', "hello world")
print(result)  # ['e', 'o', 'o']

# [a-z]+ — words from lowercase letters
result = re.findall(r'[a-z]+', "Hello World 123")
print(result)  # ['ello', 'orld']

# [^0-9] — everything EXCEPT digits
result = re.findall(r'[^0-9]+', "abc123def456")
print(result)  # ['abc', 'def']

# --- 10. | — OR ---
result = re.findall(r'cat|dog', "I have a cat and a dog and a cat")
print(result)  # ['cat', 'dog', 'cat']

# --- 11. ^ and $ — start and end of string ---
result = re.findall(r'^Hello', "Hello world")
print(result)  # ['Hello']

result = re.findall(r'^Hello', "Say Hello")
print(result)  # [] — Hello is not at the start

# --- 12. \b — word boundary ---
result = re.findall(r'\bcat\b', "cat catalog caterpillar the cat sat")
print(result)  # ['cat', 'cat'] — catalog and caterpillar didn't match

# --- 13. \s — whitespace characters ---
result = re.findall(r'\s+', "hello   world\tfoo\nbar")
print(result)  # ['   ', '\t', '\n']

# --- 14. Groups () — change findall behavior! ---
# Without groups — returns full match:
result = re.findall(r'\d+-\d+', "12-34 and 56-78")
print(result)  # ['12-34', '56-78']

# With groups — returns ONLY group contents:
result = re.findall(r'(\d+)-(\d+)', "12-34 and 56-78")
print(result)  # [('12', '34'), ('56', '78')]

# (?:...) — non-capturing group (findall returns full match):
result = re.findall(r'(?:\d+)-(?:\d+)', "12-34 and 56-78")
print(result)  # ['12-34', '56-78']

# --- 15. Greedy vs lazy matching ---
# Greedy .* — grabs as much as possible
result = re.findall(r'<.*>', "<a><b><c>")
print(result)  # ['<a><b><c>']

# Lazy .*? — grabs as little as possible
result = re.findall(r'<.*?>', "<a><b><c>")
print(result)  # ['<a>', '<b>', '<c>']

# --- 16. Lookahead (?=...) — peek ahead ---
result = re.findall(r'\d+(?= usd)', "100 usd 200 eur 300 usd")
print(result)  # ['100', '300'] — numbers followed by " usd"

# --- 17. Lookbehind (?<=...) — peek behind ---
result = re.findall(r'(?<=\$)\d+', "$50 and €30 and $100")
print(result)  # ['50', '100'] — numbers preceded by $

# ============================================
# FLAGS
# ============================================

# --- 18. re.IGNORECASE (re.I) — ignore case ---
# Without flag: exact match only
result = re.findall(r'hello', "Hello HELLO hello HeLLo")
print(result)  # ['hello']

# With flag: all case variations
result = re.findall(r'hello', "Hello HELLO hello HeLLo", re.IGNORECASE)
print(result)  # ['Hello', 'HELLO', 'hello', 'HeLLo']

# --- 19. re.MULTILINE (re.M) — ^ and $ for each line ---
text = "first line\nsecond line\nthird line"

# Without flag: only start of entire text
result = re.findall(r'^\w+', text)
print(result)  # ['first']

# With flag: start of each line
result = re.findall(r'^\w+', text, re.MULTILINE)
print(result)  # ['first', 'second', 'third']

# --- 20. re.DOTALL (re.S) — dot matches \n ---
text = "<p>\ntext\n</p>"

# Without flag: . does not match \n
result = re.findall(r'<p>.*</p>', text)
print(result)  # []

# With flag: . now matches \n too
result = re.findall(r'<p>.*</p>', text, re.DOTALL)
print(result)  # ['<p>\ntext\n</p>']

# --- 21. re.VERBOSE (re.X) — readable pattern with comments ---
# Calculator pattern, nicely formatted:
pattern = r'''
    \d+\.?\d*   # number: integer or decimal
    |           # OR
    [+\-*/]     # operator: + - * /
'''
result = re.findall(pattern, "3.14 + 2 * 10 - 7 / 3", re.VERBOSE)
print(result)  # ['3.14', '+', '2', '*', '10', '-', '7', '/', '3']

# --- 22. Combining flags with | ---
text = "Hello world\nhello Python"
result = re.findall(r'^hello', text, re.IGNORECASE | re.MULTILINE)
print(result)  # ['Hello', 'hello']

# ============================================
# BONUS: calculator pattern
# ============================================
expression = "312 + 42 / 3 * 2.5 - 1"
result = re.findall(r'\d+\.?\d*|[+\-*/]', expression)
print(result)  # ['312', '+', '42', '/', '3', '*', '2.5', '-', '1']
