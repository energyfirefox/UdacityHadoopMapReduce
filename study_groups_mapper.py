#!/usr/bin/python

import sys
import csv

# Main idea:
# Thread ID and author ID for every post in this thread should be emitted.
# If node type = question: thread_id = post_id, abs_parent_id = '\N'
# If node type = answer or comment: thread_id = abs_parent_id

def mapper():
	# read input from csv file
	reader = csv.reader(sys.stdin, delimiter = '\t')
	# skip headers
	reader.next()
	for line in reader:
		# check record, if number of fields not equal 19, something is wrong with record    		
    		if len(line) == 19:	
			author_id = line[3]

			# by default, thread_id = post_id
			thread_id = line[0]

			abs_parent_id = line[7]
			
			# if node_type is comment or answer abs_parent_id != '\N' and thread_id should be replaced by abs_parent_id
			if abs_parent_id != '\N':
				thread_id = abs_parent_id	

			# emit thread_id, author_id
			print "{0}\t{1}".format(thread_id, author_id)


def main():
	mapper()
	sys.stdin = sys.__stdin__

main()	
