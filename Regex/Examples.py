# import re
#
# text = 'geeks for geeks. Mytext is awesome 545346346'
#
# result = re.search(r"\d{9}", text)
# print(result)
import re

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'portal', s)

print('Start Index:', match.start())
print('End Index:', match.end())

# without using

# match = re.search(r'.', s)
# print(match)

# match = re.search(r'for', text)
# print(match)

# using \
# match = re.search(r'\.', s)
# print(match)