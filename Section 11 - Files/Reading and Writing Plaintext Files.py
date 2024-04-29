helloFile = open('exampleText.txt')
writingFile = open('exampleText2.txt', 'w')
content = helloFile.read()
listOfStrings = helloFile.readlines()
print(content)

writingFile.write('Hello there. Nice to meet you.')
writingFile.close()

import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Momo', 'Nana']

keys = list(shelfFile.keys())
values = list(shelfFile.values())

print(keys)
print(values)
shelfFile.close()
