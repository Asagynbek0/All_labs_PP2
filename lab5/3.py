import re

def matching_sequences(text):
    ptrn = r'^[a-z]+_[a-z]+$'
    if re.fullmatch(ptrn,text):
        return True
    else:
        return False
    
text=["salem_alem","my_name","Hey_bro","How_are","hello_friend"]

for i in text:
    print(f"{i}:{matching_sequences(i)}")