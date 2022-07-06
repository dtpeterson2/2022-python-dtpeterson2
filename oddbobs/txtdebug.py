#I copied this to show how we can locate text in files
from sys import argv    #Get an argv

count = int(0)
script, filename = argv
with open(filename,"rb") as txt:
    line=txt.readline()
    print("BOF")
    while line:
        lineInfo = f"{count:05d} [len:{len(line):05d}] [LF index: {txt.tell():05d} {line}]"
        print(lineInfo)
        count=count+1
        line = txt.readline()
    print("EOF")