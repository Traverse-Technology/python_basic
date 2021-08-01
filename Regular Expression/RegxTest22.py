import re
str24 = "Rich's password:aPPl3s345 is strong"
str31 = '146.176.123.2'
str32 = '146.176.123.8'
str33 = '146.176.123.9'
match = re.search(r'[a-z]:[a-zA-Z0-9]+', str31)
if match: print(f'found the pattern: {match.group()}')