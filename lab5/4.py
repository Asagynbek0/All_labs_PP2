import re 

def matching_sequences(text):
    ptrn=r'^[A-Z]+[a-z]+$'
    return bool(re.fullmatch(ptrn,text))

text=["Alinur","hello","How","what","Movie"]        

for i in text:
    print(f"{i}:{matching_sequences(i)}")