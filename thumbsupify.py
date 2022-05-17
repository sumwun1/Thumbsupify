import sys

if(len(sys.argv) != 3):
    print("usage: \"python3 thumbsupify.py [inFileName] [outFileName]\"")
    sys.exit(1)

fileIn = open(sys.argv[1], 'r')
fileOut = open(sys.argv[2], 'w')

for a in fileIn:
    fileOut.write(a.replace(" ", "\U0001f44d"))
