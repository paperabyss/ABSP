import os
for folderName, subfolders, filenames in os.walk('/Users/tannerking/Documents'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName  + ' are ' + str(subfolders))
    print('The filenames in ' + folderName + ' are ' +str(subfolders))
    print()
