import re
e2 = 'johncleese@montypython.com blah rich@napier.com blah'
matches = re.findall(r'(\w+)@(\w+.com)', e2)
print(type(matches))