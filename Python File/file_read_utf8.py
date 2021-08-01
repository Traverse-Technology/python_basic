f = open('good morning UTF8.txt','r', encoding='utf_8')

print(f.read())
f.seek(0)
print(f.read())

f.close()