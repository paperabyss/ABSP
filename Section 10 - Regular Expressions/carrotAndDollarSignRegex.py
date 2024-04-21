import re

beginsWithHelloRegex = re.compile(r'^Hello') # The ^ symbol indicates that the match should occur at the start of the string. 

print(beginsWithHelloRegex.search('Hello there!')) # Should find a match.
print(beginsWithHelloRegex.search('He said "Hello!"')) #Should not find a match. 

endsWithWorldRegex = re.compile(r'world!$')# The $ indicates that the match should occur at the end of the string. 

print(endsWithWorldRegex.search(r'Hello, world!')) # Should find a match.
print(endsWithWorldRegex.search(r'Hello, world! How are you today?')) #Should not find a match. 

atRegex = re.compile(r'.at') # The '.' is a symbol that matches any character. 
print(atRegex.findall('The cat in the hat sat on the flat mat'))

nameRegex = re.compile(r'Name: (.*) Class: (.*)')# .* syntax allows for easy matching of more information.

Mio = 'Name: Mio Class: Zephyr'

print(nameRegex.findall(Mio))
