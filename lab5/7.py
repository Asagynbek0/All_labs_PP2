import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s)

test_strings = [
    "hello_world",
    "my_variable_name",
    "convert_this_string",
    "example_text_here",
    "snake_case"
]

for text in test_strings:
    print(f"{text} => {snake_to_camel(text)}")
