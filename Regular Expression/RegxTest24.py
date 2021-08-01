import re
str44 = 'href="http://www.blah.com"'
match = re.search(r'http[s]?|ftp', str44)
if match: print(f'found the pattern: {match.group()}')