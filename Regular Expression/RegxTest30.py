import re
strx = 'server 146.176.123.258'
match = re.search(r'146\.176\.123\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])$', strx)
if match: print(f'found the pattern: {match.group()}')
