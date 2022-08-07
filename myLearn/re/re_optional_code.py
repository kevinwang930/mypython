import re
str1 = "test*3"
re1 = re.compile("(?P<name>[a-zA-Z]+)(?:\\*(?P<number>[0-9]))?")
result = re1.search(str1)
if result:
    print(result.group('number'))