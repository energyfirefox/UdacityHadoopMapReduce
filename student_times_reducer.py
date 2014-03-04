#!/usr/bin/python

import sys


maxPostsHour = None
oldAuthor = None
hours_post = {}


# Loop around the data
# It will be in the format key\tval
# Where key is the author_id, val is hour for post
# All the hours for a particular author_id will be presented in hours_post dictionary, where keys = hours and values = post amount of this author during particalar hour
# Then the key will change and we'll be dealing with the next author

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisAuthor, thisHour = data_mapped

    # if author id changes - emit results  and set vars to default values

    if oldAuthor and oldAuthor != thisAuthor:
        # print "{0}\t{1}".format(oldAuthor, maxPostsHour)
	print "{0}\t{1}".format(oldAuthor, max_h)
        maxPostsHour = None
        hours_post = {}
        
        

    oldAuthor = thisAuthor

    if thisHour not in hours_post.keys():
	hours_post[thisHour] = 1
    else:
	hours_post[thisHour] += 1

    # get hour (hours_post.keys()) with max value as maxPostsHour:    
    max_h = []
    maxPostsHour = max(hours_post, key=hours_post.get)
    # get all hours, which equal to max posts values and collect them in max_h list
    maxVal = hours_post[maxPostsHour]
    for k in hours_post.keys():
	if hours_post[k] == maxVal:
	    max_h.append(k)
    
    
# processing the last key
if oldAuthor != None:
    print "{0}\t{1}".format(oldAuthor, max_h)
    

 


