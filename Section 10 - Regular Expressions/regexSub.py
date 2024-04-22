import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

editedNamesRegex = re.compile(r'Agent (\w)\w*') #This edited regex will only return the first group (the (\w)). In this case it will return the first letter after 'Agent '.
print(editedNamesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))#The \1 indicates that sub should use the first group from the edited name Regex to replace the match. 
