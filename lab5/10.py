import re

def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

test_strings = [
    "helloWorld",
    "myVariableName",
    "convertThisString",
    "exampleTextHere",
    "snakeCase"
]

for text in test_strings:
    print(f"{text} => {camel_to_snake(text)}")
