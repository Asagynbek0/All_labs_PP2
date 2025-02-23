import re

def matching_b_let(text):
    ptrn = r'^a.*b$'
    return bool(re.fullmatch(ptrn,text))

text = ["ab","axb" ,"bac","cab","anythingb","a12345b"]
for i in text:
    print(f"{i}:{matching_b_let(i)}")