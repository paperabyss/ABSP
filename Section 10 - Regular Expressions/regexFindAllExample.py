import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = (r'Call me at 111-222-3333 or at my office number at 222-333-4444')

print(phoneRegex.search(message))
print(phoneRegex.findall(message))

groupedPhoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(groupedPhoneRegex.findall(message))

lyrics = '''
12 drummers drumming,
11 pipers piping,
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
4 French hens,
3 turtle doves,
And 1 partridge in a pear tree!
'''

xmasRegex = re.compile(r'\d+\s\w+')

print(xmasRegex.findall(lyrics))


vowelRegex = re.compile(r'[aeiouAEIOU]{2}')

print(vowelRegex.findall('Lance wants something a bit meatier'))
