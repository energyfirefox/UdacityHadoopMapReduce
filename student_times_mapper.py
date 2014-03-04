#!/usr/bin/python

import sys
import csv

# Main idea:
# Author ID  and hour for every post should be emitted.
# Hour has definite position in date/time string (11 and 12 symbols)


def mapper():
	# read input from csv file
	reader = csv.reader(sys.stdin, delimiter = '\t')
	# skip headers
	#reader.next()
	
	for line in reader:  
		# check record, if number of fields not equal 19, something is wrong with this record   		
    		if len(line) == 19:	
			author_id = line[3]
			hour = line[8][11:13]			
			# emit author_id, hour:			
			print "{0}\t{1}".format(author_id, hour)


def main():
	mapper()
	sys.stdin = sys.__stdin__

main()	
