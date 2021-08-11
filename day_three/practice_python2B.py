#!/usr/bin/env python3

import sys

IN = open(sys.argv[1], 'r')
	
CTR = 0
OUT = open("outfile.txt", 'w')

for Line in IN:
	Line_clean = Line.strip("\n")
	print(Line_clean)
	Line_length = len(Line_clean)
	print(Line_length)
	CTR += 1
	#print(CTR)
	OUT.write("Line number: %d,Line length: %d \n" % (CTR, Line_length))

IN.close()
OUT.close()

#    OUT.write("Line length: ", Line_length)
    
    
	