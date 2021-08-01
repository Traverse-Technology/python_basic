f = open(r'foods.txt')

for line in f:
	if "\n" in line:
		print(line.rstrip('\n'))
	else:
		print(line)

f.close()