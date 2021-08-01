import re
str31 = '146.176.123.2'
str32 = '146.176.123.8'
str33 = '146.176.123.9'
match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', str33)
if match: print(f'found the pattern: {match.group()}')
