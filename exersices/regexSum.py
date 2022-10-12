"""
Count all sum of all digits in file by regex extracting
"""
import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum.txt"
handle = open(name)
sumList = list()
for line in handle:
    line = line.rstrip()
    num = re.findall('\d+', line)
    numInt = map(int, num)
    sumList.extend(numInt)
sumNum = sum(sumList)
print(f'{sumNum}')


