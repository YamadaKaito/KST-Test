import sys
import os.path

# initialization
inputFile = sys.argv[1] # get the filename from the argument value
outputFile = "sorted-name-list.txt" # naming the output file
subList = []

# get the indexed name
def subName(name, idx):
    idx -= 1 # balanced life
    result = name.split() # split the name with (default) <space> separator
    while idx >= len(result): # get the prefix name when no third name
        idx -= 1
    return result[idx]

# sorting
def sorting():
    tempList = []
    with open(inputFile) as f: # open the input file
        for line in f: # foreach
            result = line.rstrip("\r\n") # remove the newLine
            tempList.append([subName(result, 3), subName(result, 1), result]) # adding multiple index key into temporary list
    tempList = sorted(tempList, key = lambda x: (x[0], x[1]), reverse = False) # sort list by multiple key
    # print(tempList) # for cheking purpose
    return tempList

# print to screen & write to file
def printWrite(slist):
    f = open(outputFile, "w+") # open & overwrite the output file
    for s in slist: # foreach
        print(s[2]) # print to screen
        f.write("%s\n" %s[2]) # write to file
    f.close() # close the output file

# check the input file & tailored all process into one
if (os.path.isfile(inputFile)):
    print("::::::::::::::::::RESULT::::::::::::::::::")
    subList = sorting()
    printWrite(subList)
    print(":::::::::::::::::::DONE:::::::::::::::::::")
else:
    print("'%s' was not found in this directory or the file can not be processed" %inputFile)
