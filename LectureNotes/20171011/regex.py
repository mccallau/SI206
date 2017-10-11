import re

test = "C00K33Z! r g..t}"

obj = re.findall("[a-zA-Z]*\s*",test)
print(obj)
