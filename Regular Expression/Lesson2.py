import re
str1 = 'string to be searched for the word parrot'

match = re.search('searched', str1)
if match:
    offset_t = match.span()
    offset_s = ''.join(str(offset_t))
    print(offset_s.strip("()"))
    print(f'found the pattern: {match.group()}')
    print(f'Found: "{match.group()}" between offsets {str(match.span()).strip("()").replace(","," and")}')
