import re
text = "HELLO world"
result = re.search(r'hello', text, re.I)
print(result)  # Output: <re.Match object; span=(0, 5), match='HELLO'>
