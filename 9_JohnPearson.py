# John Pearson
# CS 100 2020F Section 111
# HW 09, October 29, 2020

#1
# inF = 'created_equal.txt'
# outF = 'copy.txt'
# def file_copy(in_file, out_file):
#     in_file = open(in_file, 'r')
#     out_file = open(out_file, 'w')
#     copy = in_file.read()
#     out_file.write(copy)
#     in_file.close
#     out_file.close
#   
# file_copy(inF, outF)

#2
# file = 'created_equal.txt'
# def file_stats(in_file):
#     infile = open(in_file, 'r')
#     infile2 = open(in_file, 'r')
#     Lines = infile.readlines()
#     numOfLines = len(Lines)
#     fileReader = infile2.read()
#     numOfWords = len(fileReader.split())
#     infile.close()
#     print('Lines ' + str(numOfLines))
#     print('Words ' + str(numOfWords))
#     print('Characters ' + str(len(fileReader)))
# file_stats(file)


#3 ! DID NOT FINISH 3 !
# inF = 'catInTheHat.txt'
# outF = 'catRepWords.txt'
# def repeat_words(in_file, out_file):
#     infile = open(in_file, 'r')
#     infile2 = open(in_file, 'r')
#     outfile = open(out_file, 'w')
#     fileReader = infile2.read1()
#     lines = infile.readlines()
#     words = fileReader.split()
#     newList=[]
#     finalCopy=[]
#     for i in words:
#         newList.append(i.lower())
#         for w in newList:
#             if newList.count(w) >= 2:
#                 if w not in finalCopy: 
#                     finalCopy.append(w)
#                     for b in finalCopy:
#                         outfile.write(b + " ")
#     print(newList)
# repeat_words(inF, outF)