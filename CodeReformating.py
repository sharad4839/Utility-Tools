import os

fileNameList = os.listdir()

for x in range(len(fileNameList)):
    print(f'{x}.\t{fileNameList[x]}')

# fileSrNo = int(input('Enter File Sr No.: '))

fileSrNo = 1

data = ''

with open(fileNameList[fileSrNo]) as file:
    data = file.read()

tabCount = 0

result = ''

for x in data:
    if x == '(':
        tabCount += 1
        result = result + '(\n' + ':\t' * tabCount
    elif x == ',':
        result = result + ',\n' + ':\t' * tabCount
    elif x == ')':
        tabCount -= 1
        result = result + '\n' + ':\t' * tabCount + ')'
    else:
        result += x

with open("result.txt",'w') as res:
    res.write(result)

print('Done')

