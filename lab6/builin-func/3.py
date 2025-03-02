def is_palindrom(string):
    return string == string[::-1]
    
string=input("txt = ")
if is_palindrom(string):
    print("Is palindrom")
else:
    print("Is not ")