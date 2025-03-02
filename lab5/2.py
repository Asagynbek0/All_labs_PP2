import re

def match_string(text):
    ptrn = r'ab{2,3}$'
    
    if re.search(ptrn,text):
        return True
    else:
        return False

text=["ab","a","aab","abb","aaaabb","abbbb", "abbb"]

for i in text:
    print(f"{i}:{match_string(i)}")