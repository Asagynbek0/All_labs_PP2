def reverse_sentence(s):
    words=s.split()
    revesed_words=words[::-1]
    return " ".join(revesed_words)
    
str=input("inpur string : ")
result=reverse_sentence(str)
print(result)