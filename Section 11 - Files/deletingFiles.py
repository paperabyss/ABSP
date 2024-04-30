import os
import shutil
os.rmdir('/Users/tannerking/Documents/ExampleFolder') ## Deletes an empty folder.

## shutil.rmtree('ExampleFolder') ## Deletes a folder and all folders and files inside.


import send2trash

send2trash.send2trash('/Users/tannerking/Documents/exampleText.txt') #the send2trash module will put any files into the os' trash instead of permanently deleting them.
