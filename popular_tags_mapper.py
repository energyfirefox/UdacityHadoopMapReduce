#!/usr/bin/python

import sys
import csv

# Main_idea: Top 10 most popular tags should be emitted.


def mapper():
	
	# dictionary for collected all tags  and counting all tags in mapper:
	all_tags = {}

	# read input from csv file
	reader = csv.reader(sys.stdin, delimiter = '\t')
	# skip headers
	reader.next()

	for line in reader:  
		# check record, if number of fields not equal 19, something is wrong with this record   		
    		if len(line) == 19:
			post_id = line[0]				
			tag_names = line[2]
			# get all tags
			tags = tag_names.split()
			for tag in tags:						
				if tag not in all_tags.keys():
				# if we need ordering by some weighting score here we can define some condition and weigths for this factor, for example if tag in [ud617, unit8-7-final] then all_tags[tag] += 1*weighted_factor, where weighted_factor = 0.8
					all_tags[tag] = 1
				else:
					all_tags[tag] += 1
	
	# sorting all tags by popularity in decreasing order:
	top_tags_indices = sorted(all_tags, key=all_tags.get, reverse = True)
	
	# emit top 10 most popular tags:	
	for tag in top_tags_indices[0:10]:
		print "{0}\t{1}".format(tag, all_tags[tag])

					


def main():
	mapper()
	sys.stdin = sys.__stdin__

main()	
