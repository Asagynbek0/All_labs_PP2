import re

def replace_symbol(text):
    ptrn=r'[ .,]'
    return re.sub(ptrn,":",text)

text = [
    "Hello, world. How are you?",
    "Python is, awesome. Really!",
    "One, two. Three four.",
    "NoSymbolsHere"
]

for i in text:
      print(f"Before: {i}")
      print(f"After:  {replace_symbol(i)}")
      print()