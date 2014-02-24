#!/usr/bin/python

import sys

# default values

totalLen = 0
totalAnswers = 0
meanAnswLength = 0
postLength = 0
oldThread = None


# Loop around the data
# It will be in the format key\tval1\tval2
# Where key is the thread_id, val1 is node_type ('question' or 'answer'), val2 is length of the post
#
# All the questions and answers for a particular thread will be presented,
# then the key(thread id) will change and we'll be dealing with the next thread

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisThread, thisNodeType, thisLength = data_mapped

    if oldThread and (oldThread != thisThread):
	# emit rows
        print "{0}\t{1}\t{2}".format(oldThread, postLength, meanAnswLength)
        # set variables to default values 
        totalAnswers = 0
        totalLen = 0
	meanAnswLength = 0
       
        
        

    oldThread = thisThread
    
    if 'answer' in thisNodeType:
	totalLen += float(thisLength)
	totalAnswers += 1
	
    if 'question' in thisNodeType:
	postLength = thisLength

    #  for questions, which has answers, count average length of answers
    if totalAnswers > 0:
	meanAnswLength = totalLen/totalAnswers

# processing the last key
if (oldThread != None):
    print "{0}\t{1}\t{2}".format(oldThread, postLength, meanAnswLength)
    


