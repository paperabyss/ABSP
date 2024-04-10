example = ["ants", "dogs", "badgers", "dogs", "elephants"]
print(example)
example.sort()
print(example)

example.append("Zebra")
print(example)
example.sort()
print(example)

example.sort(key=str.lower)
print(example)
