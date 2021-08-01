import re
str17 = 'string to be (0)131 445 3665 searched, for phone number'
str21 = '(0)131-445-3665'
str22 = '(0)131 445-3665'
str23 = '01314451633'

match = re.search(r'\d+[- ]?\d+', str21)
if match: print(f'found the pattern: {match.group()}')