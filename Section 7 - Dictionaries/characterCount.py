import pprint
message = 'Sometimes, a person reaches a point in their life when it becomes absolutely essential to get the fuck out of the city.'
count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] += 1

pprint.pprint(count)
    
