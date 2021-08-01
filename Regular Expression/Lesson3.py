import re
str1 = 'string to be searched for the word parrot'
match = re.search(r'p\w\w\w\w\w', str1)
if match:
    print(f'found the pattern: {match.group()}')
print(match)