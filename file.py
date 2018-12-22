import os

def discoverdirbranch(path):
    for dirName, subdirList, fileList in os.walk(path):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)

