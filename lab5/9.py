import re
text = "whatYourNameAlinurToMeetYou"
space = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(space)