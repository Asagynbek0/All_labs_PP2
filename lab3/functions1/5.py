def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]  
        permute(new_s, answer + s[i])  
        
str = input("Input string: ")
permute(str)
