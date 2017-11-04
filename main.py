import sys
import os
import re

'''
A script to count all my words, because I can't help myself.
Read anything in the format 'game-n' where n is an integer of 0 or more
So it should read folders and also files.
I want to try and avoid the -notes files.
'''


def main():
    with open('game-1/game-1.md', mode='r') as rawFile:
        mdFile = rawFile.read()
        words = word_count(mdFile)
        print(words)


def word_count(mdFile):
    if type(mdFile) is not str:
        print("Couldn't read file")
        return 0
    splitOutput = mdFile.split()
    return len(splitOutput)


if __name__ == "__main__":
    main()
