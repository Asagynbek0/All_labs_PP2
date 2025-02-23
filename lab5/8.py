import re
text = "WhatYourNameAlinurToMeetYou"
spl = re.findall(r'[A-Z][^A-Z]*', text)
print(spl)