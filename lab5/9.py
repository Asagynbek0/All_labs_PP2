import re 
text = "helloJohnMyNameIsAlikhan"
x = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(x)
