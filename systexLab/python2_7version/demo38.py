# encoding=UTF-8
import os
import sys

print os.getcwd()

path1 = u'臨時目錄'
os.mkdir(path1)
os.chdir(path1)
print os.getcwd().decode('ms950')
os.chdir('..')
os.rmdir(path1)

print "python executable in:", sys.executable

for arg in sys.argv:
    print arg