import re

def match_string(text):
    ptrn = r'a*b+'
    
    if re.fullmatch(ptrn,text):
        return True
    else:
        return False

text=["ab","a","aab","abb","aaaabb","b","c"]

for i in text:
    print(f"{i}:{match_string(i)}")