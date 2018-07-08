"""
/Build-1.dmg
/Build-2.dmg
/Build-2.1.dmg
/Build-2.1.1.dmg
/Build-3.dmg
/Build-3.2.dmg
/Build-3.19.dmg

Write a script that takes a path to the folder as an argument,
and prints the highest build number (just the number, i.e. 2.1.1)
Note:  The first digit can go up to 999 and should always be present,
but the second and third can only go up to 99, and might not be included.
"""

import argparse
import sys
import re
import os

parser = argparse.ArgumentParser(description='Process build path')
parser.add_argument('-path', help='Use following convention: sortBuilds.py -path PATH_OF_DMG_FILES')
args = parser.parse_args()

buildPath = sys.argv[2]
fileList = os.listdir(buildPath)

# print("Files present in build path: ")
# print(fileList)

allVersionNumbers = []
for value in fileList:
    versionNumber = re.sub('[A-Za-z-]', '',  value)
    if versionNumber.endswith('.'):
        versionNumber = versionNumber[:-1]
    allVersionNumbers.append(versionNumber)
print('\n')
print("Build files found:")
for myFile in fileList:
    print(myFile)

print('\n')
# ^([0-9]){0,3}(\.){0,1}([0-9]){0,2}(\.){0,1}([0-9]){0,2}$
pattern = re.compile('^([0-9]){0,3}(\.)?([0-9]){0,2}(\.)?([0-9]){0,2}$')
trueVersionNumber = list(filter(pattern.match, allVersionNumbers))

trueVersionNumber.sort()
print("Valid build files:")
for value in trueVersionNumber:
    print(value)




