import re
e1 = 'johncleese@montypython.com'
match = re.search(r'(\w+)@(\w+.com)', e1)
if match: 
	print(f'found the pattern: {match.group(2)}')