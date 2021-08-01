import re
e1 = "abbbepebbbb"
match = re.search(r'[a][A-Za-z]*epe[A-Za-z]*y$' , e1)
if match: print(f'found the pattern: {match.group()}')