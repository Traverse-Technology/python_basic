f = open("foods.txt", "r")

print(f.read())
f.seek(0)
print(f.read())

f.close()