import os

totalSize = 0
directory = input

for fileName in os.listdir('/Users/tannerking/Documents'):
    if not os.path.isfile(os.path.join('/Users/tannerking/Documents', fileName)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/tannerking/Documents', fileName))


print(totalSize)
