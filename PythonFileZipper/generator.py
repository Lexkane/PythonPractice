from enum import Enum
import random


def main():
    pass


class Foo(Enum):
    Bouquet = 0
    Cactus = 1
    Flower = 2
    Flowerpot = 3
    Palm = 4


g1 = random.choice(enumerate(list(Foo)))
g2 = random.choice(range(100))

for x, y in zip(g1, g2):
    print(x[0]+y[0])


import sys

allFIles=sys.argv
filePosition=1
fileData=[]

while filePosition<len(allFIles)
	with open(allFiles[filePosition],'r') as fileData
		fileData.append(Data.read())
	filePosition+=1

newFileName=input("Enter file name to save:")

with open (newFileName,'w') as newFile:
	newFile.write("".join(fileData))		