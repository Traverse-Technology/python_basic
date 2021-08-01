import re
e2 = 'johncleese@montypython.com blah rich@napier.com blah'
matches = re.findall(r'\w+@\w+.com', e2)
if matches: print(f'found the pattern: {matches}')
print(matches)