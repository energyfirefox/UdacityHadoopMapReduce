#!/usr/bin/python

import sys

all_tags = {} 


# Loop around the data
# It will be in the format key\tval
# Where key is tag, val is the amount of this tag in the posts
# Top 10 most popular tags should be emitted
# actually, the reducer is quite tha same as the mapper for this task

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisTag, thisValue = data_mapped  	
					
    if thisTag not in all_tags.keys():
    	all_tags[thisTag] = float(thisValue)
    else:
	all_tags[thisTag] += float(thisValue)

# sorting all tags by popularity in decreasing order:
top_tags_indices = sorted(all_tags, key=all_tags.get, reverse = True)

# emit top 10 most popular tags:	
for tag in top_tags_indices[0:10]:
	print "{0}\t{1}".format(tag, all_tags[tag])


