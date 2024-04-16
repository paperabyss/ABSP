import re

message = "Call me at 111-111-1112"

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group(1))
