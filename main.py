import sys
import os

'''
A script to count all my words, because I can't help myself.
Read anything in the format 'game-n' where n is an integer of 0 or more
So it should read folders and also files.
I want to try and avoid the -notes files.
Maybe some other time....
'''

filePaths = ['game-1/game-1.md', 'game-2/game-2.md', 'game-3/game-3.md', 'game-4/game-4.md',
             'game-5/game-5.md', 'game-6/game-6.md', 'game-7/game-7.md', 'game-8/game-8.md']


def main():
    wordTotal = 0

    for path in filePaths:
        with open(path, mode='r') as rawFile:
            mdFile = rawFile.read()
            wordTotal += word_count(mdFile)

    print(wordTotal)


def word_count(mdFile):
    if type(mdFile) is not str:
        print("Couldn't read file")
        return 0
    splitOutput = mdFile.split()
    return len(splitOutput)


if __name__ == "__main__":
    main()
