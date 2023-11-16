def numLines(filename):
    '''return the number of      lines in filename'''
    infile = open(filename, 'r')
    lineList = infile.readlines()
    infile.close()
    return len(lineList)
print(numLines('created_equal.txt'))