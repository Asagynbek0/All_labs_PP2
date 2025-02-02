def is_palindrome(text):
    text = text.lower().replace(" ", "")  
    return text == text[::-1]

res=input("Input sentence : ")

print(is_palindrome(res))
