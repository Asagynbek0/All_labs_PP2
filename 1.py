import re
text="Price:5000tg,num=10`"
pattern=r"[0-9][,]"
result=re.findall(pattern,text)
print(result)