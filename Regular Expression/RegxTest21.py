import re
str21 = 'john@cleese.com'
str22 = 'john.cleese@montypython.com'
str23 = 'michael-palin@python.co.uk'

match = re.search(r'\w+[-.]?\w*@\w*.\w+\w?', str21)
if match: print(f'found the pattern: {match.group()}')
