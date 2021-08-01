import re
str1 = 'string to be searched for the word parrot'

match = re.search('parrot', str1)
print(match)
print(match.group())
print(type(match.span()))