import re

str1 = "Packets: Sent = 2, Received = 0, Lost = 2 (100 % loss),"
# received_packages = re.compile(r".*Received[\s]*=[\s]*(?P<n>[0-9]+)")
received_packages = re.compile(r"Received[\s]*=[\s]*(?P<n>[0-9]+)")
result = received_packages.search(str1)
if result:

    print(result.group('n'))
    # print(result.groupdict())
    # print(result[0])
