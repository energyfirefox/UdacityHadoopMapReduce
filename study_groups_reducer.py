#!/usr/bin/python

import sys

# default values

maxPostsHour = None
oldThread = None
threads_authors = []

# Loop around the data
# It will be in the format key\tval
# Where key is the thread id, val is the author id
#
# All the authors_id's for a particular thread will be presented and collected in list thread_authors,
# then the key(thread_id) will change and we'll be dealing with the next thread_id

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisThread, thisAuthor = data_mapped


    # if thread id changes - emit resulst for previous thread and set thread_authors to empty list 
    if oldThread and oldThread != thisThread:
        print "{0}\t{1}".format(oldThread, threads_authors)       
        threads_authors = []           
        

    oldThread = thisThread
    # append authors_id to thread authors list
    threads_authors.append(thisAuthor)

# processing the last key
if oldThread != None:
    print "{0}\t{1}".format(oldThread, threads_authors)
 


