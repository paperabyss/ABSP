import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

editedNamesRegex = re.compile(r'Agent (\w)\w*') #This edited regex will only return the first group (the (\w)). In this case it will return the first letter after 'Agent '.
print(editedNamesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))#The \1 indicates that sub should use the first group from the edited name Regex to replace the match.


re.compile(r'''
(\d\d\d-) |    # area code with dash
(\ (\d\d\d) )  # area code with no dash but with parens
\d\d\d         # first three digits
-              # dash
\d\d\d\d       # last 4 digits''', re.VERBOSE) #Passing the verbose argument to the compiler tells it that white space and new lines should be ignored and aren't apart of the pattern we are trying to match. Makes it nicer to read and easier to comment on.
