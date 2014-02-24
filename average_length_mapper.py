#!/usr/bin/python


# Main idea: node_id = post_id, if node_type is answer - node_id is replaced by abs_parent_id
# only nodes with node_type 'question' or 'answer' should be emitted
# emitted values: node_id, node_type, length of post (length of posts body)

import sys
import csv

def mapper():
	
	# read input from csv file
	reader = csv.reader(sys.stdin, delimiter = '\t')
	# skip header
	reader.next()

	for line in reader:    
		# check record, if number of fields not equal 19, something is wrong with this record  		
    		if len(line) == 19:	
			post_id = line[0]
			body = line[4]			
			abs_parent_id = line[7]
			node_type = line[5]
			
			# if node_type = 'answer', replace post_id by abs_parent_id
			if 'answer' in node_type:
	    			post_id = abs_parent_id
			
			# if length of body == 0 then it is not valid post; skip comments
			if ('comment' not in node_type) and len(body) > 0:
				# emit post_id, node_type and length of posts for questions and answers
				print "{0}\t{1}\t{2}".format(post_id, node_type, len(body))


def main():
	mapper()
	sys.stdin = sys.__stdin__

main()	
