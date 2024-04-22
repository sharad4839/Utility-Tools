import os

fileNameList = os.listdir()

for x in range(len(fileNameList)):
    print(f'{x}.\t{fileNameList[x]}')

fileSrNo = int(input('Enter File Sr No.: '))

# fileSrNo = 1

data = ''

with open(fileNameList[fileSrNo]) as file:
    data = file.read()

result = data.replace('\n',' ').replace(' ' * 4, '')

with open("result.txt",'w') as res:
    res.write(result)

print('Done')

