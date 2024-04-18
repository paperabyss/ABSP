import re
regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))

haRegex = re.compile(r'(Ha){3,5}')

print(haRegex.search('He said "HaHaHaHa"'))

greedyRegex = re.compile(r'(\d){3,5}')

nonGreedyRegex = re.compile(r'(\d){3,5}?')

print(greedyRegex.search('1234567890'))
print(nonGreedyRegex.search('1234567890'))
