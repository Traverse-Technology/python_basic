import re
e2 = 'johncleese@montypython.com blah rich@napier.com blah'
match = re.search(r'\w+@\w+.com', e2)
if match: print(f'found the pattern: {match.group()}')