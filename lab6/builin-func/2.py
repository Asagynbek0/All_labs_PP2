

def calculate(string1):
    upper_c=sum(1 for char in string1 if char.isupper() )
    lower_c=sum(1 for char in string1 if char.islower() )
    print("upper_c letters: ",upper_c)
    print("lowe_c letters: ",lower_c)
    
string1="HowAreYou"

calculate(string1)